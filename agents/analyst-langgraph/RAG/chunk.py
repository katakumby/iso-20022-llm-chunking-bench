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
import os
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')

load_dotenv(dotenv_path)



input_directory = sys.argv[1] #file path from command line
collection_prefix = sys.argv[2] #file path from command line
chunking_strategy = sys.argv[3] #chunking strategy: "markdownHeaderTextSplitter" or "header"
chunk_config = sys.argv[4].split(":") #{chunk_size}:{chunk_overlap} e.g. 500:30
embeddings_model = os.getenv('EMBEDDINGS_MODEL')

input_endoding = "utf8"
# input_endoding = "windows-1252"

print(f"Running with params: collection_prefix:{collection_prefix} input_directory:{input_directory} chunking_strategy:{chunking_strategy} chunk_config:{int(chunk_config[0])}:{int(chunk_config[1])} embeddings_model:{embeddings_model}")
# E:\AI\DocVec\inputs\iso20022org
# E:\AI\DocVec\outputs
# E:\AI\DocVec\a2a-samples\samples\python\agents\langgraph\RAG\data\eventcatalog


embeddings = OllamaEmbeddings(model=embeddings_model)
# embeddings = LocalAIEmbeddings(
#     openai_api_key="random-string",
#     # openai_api_base=os.getenv('API_BASE'),
#     openai_api_base="http://localhost:11434/v1",
#     model="text-embedding-qwen3-embedding-0.6b",
# )


qdrant_api = os.getenv('QDRANT_API')

def markdownHeaderTextSplitter(file,file_encoding = "utf8", headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]):
    try:
        with open(file, encoding=file_encoding) as f:
            markdown_document = f.read()
    except:
        with open(file, encoding="windows-1252") as f:
            markdown_document = f.read()    
    # markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

    md_header_splits = markdown_splitter.split_text(markdown_document)

    for doc in md_header_splits:
        if hasattr(doc, "metadata"):
            doc.metadata["source_file"] = os.path.basename(markdown_file)
    return md_header_splits

def unstructuredMarkdownLoader(file,mode = "single"):
    loader = UnstructuredMarkdownLoader(file,mode=mode)
    data = loader.load()
    return data

def semanticChunker(file,file_encoding = "utf8"):
    try:
        with open(file, encoding=file_encoding) as f:
            content = f.read()
    except:
        with open(file, encoding="windows-1252") as f:
            content = f.read()   
    text_splitter = SemanticChunker(embeddings, breakpoint_threshold_type="percentile",breakpoint_threshold_amount=95.0, min_chunk_size=200)
    docs = text_splitter.create_documents([content])
    for doc in docs:
        if hasattr(doc, "metadata"):
            doc.metadata["source_file"] = os.path.basename(markdown_file)
    return docs

for root, dirs, files in os.walk(input_directory):
    for file in files:
        markdown_file = os.path.join(root, file)
        if not markdown_file.endswith('.md'):
            continue
        #get subfolder directory for file relative to input_directory
        relative_dir = os.path.relpath(root, input_directory)

        print(f"Processing file: {markdown_file} from (sub-)domain: {relative_dir}")

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

        if(relative_dir != "."):
            for doc in md_header_splits:
                if hasattr(doc, "metadata"):
                    doc.metadata["path"] = relative_dir
        
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
            url=qdrant_api,
            prefer_grpc=True,
            api_key="<---api key here--->",
            collection_name=f"{collection_prefix}_{chunking_strategy}",
        )
        print(f"Finished processing: {markdown_file}")
