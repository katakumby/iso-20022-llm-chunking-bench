from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter
# from langchain_text_splitters.markdown import MarkdownTextSplitter
# from langchain_text_splitters.markdown import LineType
# from langchain_text_splitters.markdown import HeaderType
# from langchain_text_splitters.markdown import HeaderType
# from langchain_text_splitters.markdown import ExperimentalMarkdownSyntaxTextSplitter
from langchain.text_splitter import MarkdownTextSplitter

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import LocalAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_experimental.text_splitter import SemanticChunker
from os.path import join, dirname
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
import uuid
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
import sys
import json
import boto3
import tempfile
import os
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')

load_dotenv(dotenv_path)



directory_prefix = sys.argv[1] #file path from command line
collection_prefix = sys.argv[2] #file path from command line
chunking_strategy = sys.argv[3] #chunking strategy: "markdownHeaderTextSplitter" or "header"
chunk_config = sys.argv[4].split(":") #{chunk_size}:{chunk_overlap} e.g. 500:30
embeddings_model = os.getenv('EMBEDDINGS_MODEL')

input_endoding = "utf8"
# input_endoding = "windows-1252"

print(f"Running with params: collection_prefix:{collection_prefix} input_directory:{directory_prefix} chunking_strategy:{chunking_strategy} chunk_config:{int(chunk_config[0])}:{int(chunk_config[1])} embeddings_model:{embeddings_model}")
# E:\AI\DocVec\inputs\iso20022org
# E:\AI\DocVec\outputs
# E:\AI\DocVec\a2a-samples\samples\python\agents\langgraph\RAG\data\eventcatalog


embeddings = OpenAIEmbeddings(
        model=os.getenv('EMBEDDINGS_MODEL'),
        base_url=os.getenv('EMBEDDINGS_BASE_URL'),
        api_key=os.getenv('EMBEDDINGS_API_KEY')
    )


def markdownHeaderTextSplitter(file,file_encoding = "utf8", headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]):
    # try:
    #     with open(file, encoding=file_encoding) as f:
    #         markdown_document = f.read()
    # except:
    #     with open(file, encoding="windows-1252") as f:
    #         markdown_document = f.read()
    #
    markdown_document = download_s3_object_to_variable(os.getenv('S3_BUCKET'), file)

    # markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

    md_header_splits = markdown_splitter.split_text(markdown_document)

    for doc in md_header_splits:
        if hasattr(doc, "metadata"):
            doc.metadata["source_file"] = os.path.basename(markdown_file)
    return md_header_splits

def unstructuredMarkdownLoader(file,mode = "single"):
    text = download_s3_object_to_variable(os.getenv('S3_BUCKET'), file)

    suffix = os.path.splitext(file)[1]  # optional: keep original extension
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    data = text.encode("utf-8")
    temp_file.write(data)
    temp_file.flush()
    temp_file.close()

    loader = UnstructuredMarkdownLoader(temp_file.name,mode=mode)
    data = loader.load()
    return data

def semanticChunker(file,file_encoding = "utf8"):
    # try:
    #     with open(file, encoding=file_encoding) as f:
    #         content = f.read()
    # except:
    #     with open(file, encoding="windows-1252") as f:
    #         content = f.read()
    content = download_s3_object_to_variable(os.getenv('S3_BUCKET'), file)
    print(content)
    text_splitter = SemanticChunker(embeddings, breakpoint_threshold_type="percentile",breakpoint_threshold_amount=95.0, min_chunk_size=200)
    docs = text_splitter.create_documents([content])
    # for doc in docs:
    #     if hasattr(doc, "metadata"):
    #         doc.metadata["source_file"] = os.path.basename(markdown_file)
    return docs

def download_dir(client, resource, dist, local='/tmp', bucket='your_bucket'):
    paginator = client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                download_dir(client, resource, subdir.get('Prefix'), local, bucket)
        for file in result.get('Contents', []):
            dest_pathname = os.path.join(local, file.get('Key'))
            if not os.path.exists(os.path.dirname(dest_pathname)):
                os.makedirs(os.path.dirname(dest_pathname))
            if not file.get('Key').endswith('/'):
                resource.meta.client.download_file(bucket, file.get('Key'), dest_pathname)

def download_s3_object_to_variable(bucket_name: str, object_key: str):
    """
    Downloads an S3 object and returns its contents as bytes.
    Works for any file type (text, binary, etc.).
    """
    s3 = boto3.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=object_key)

    # Read the object body into memory
    data = response["Body"].read()   # returns bytes
    try:
        text = data.decode("utf-8")
        return text
    except UnicodeDecodeError:
        text = data.decode("windows-1252")
        return text

client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('S3_AKID'),
    aws_secret_access_key=os.getenv('S3_SK'),
    region_name="eu-north-1"
)
s3_resource = boto3.resource('s3')

my_bucket = s3_resource.Bucket(os.getenv('S3_BUCKET'))



for objects in my_bucket.objects.filter(Prefix=directory_prefix):
    print(objects)


# for root, dirs, files in os.walk(input_directory):
for objects in my_bucket.objects.filter(Prefix=directory_prefix):
    # for file in files:
        markdown_file = objects.key
        if not markdown_file.endswith('.md'):
            continue
        #get subfolder directory for file relative to input_directory
        key_without_prefix = objects.key.lstrip(f'${directory_prefix}/')
        domain_name = key_without_prefix.split('/')[0]
        if(domain_name == key_without_prefix):
            domain_name = None


        print(f"Processing file: {key_without_prefix} from (sub-)domain: {domain_name}")

        match chunking_strategy:
            case "markdownHeaderTextSplitter":
                md_header_splits = markdownHeaderTextSplitter(markdown_file,input_endoding)
            case "unstructuredMarkdownLoaderSingle":
                md_header_splits = unstructuredMarkdownLoader(markdown_file,"single")
            case "unstructuredMarkdownLoaderElements":
                md_header_splits = unstructuredMarkdownLoader(markdown_file,"elements")
            case "semanticChunker":
                md_header_splits = semanticChunker(markdown_file)
            case _:
                raise ValueError(f"Unknown chunking strategy: {chunking_strategy}")


        for doc in md_header_splits:
            if hasattr(doc, "metadata"):
                doc.metadata["s3key"] = objects.key
                if (domain_name != None):
                    doc.metadata["domain"] = domain_name

        chunk_size = int(chunk_config[0])
        chunk_overlap = int(chunk_config[1])

        if(chunk_size != 0):
            for doc in md_header_splits:
                if hasattr(doc, "metadata"):
                    doc.metadata["_chunk_id"] = str(uuid.uuid4())
            # text_splitter = RecursiveCharacterTextSplitter(
            #     chunk_size=chunk_size, chunk_overlap=chunk_overlap, separators=["\n\n", "\n", ".", " ", ""]
            # )
            # text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            text_splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            final_documents = text_splitter.split_documents(md_header_splits)
        else:
            final_documents = md_header_splits


        qdrant = QdrantVectorStore.from_documents(
            final_documents,
            embeddings,
            url=os.getenv('QDRANT_API'),
            prefer_grpc=True,
            api_key=os.getenv('QDRANT_API_KEY'),
            collection_name=f"{collection_prefix}_{chunking_strategy}",
        )
        print(f"Finished processing: {markdown_file}")
