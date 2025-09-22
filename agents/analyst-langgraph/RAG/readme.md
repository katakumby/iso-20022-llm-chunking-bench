

# How to


Load, chunk, process and push documents into database

Avaiable strategies:
    - markdownHeaderTextSplitter
    - unstructuredMarkdownLoaderSingle
    - unstructuredMarkdownLoaderElements
    - semanticChunker
```powershell

Set-Variable -Name "basedir" -Value "E:\\AI\\DocVec"

#For ISO20022 Material isomarkitdown
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdown markdownHeaderTextSplitter 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdown unstructuredMarkdownLoaderSingle 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdown unstructuredMarkdownLoaderElements 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdown semanticChunker 500:30

#For ISO20022 Material markitdown_plugin
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdownplug markdownHeaderTextSplitter 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdownplug unstructuredMarkdownLoaderSingle 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdownplug unstructuredMarkdownLoaderElements 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\markitdown_plugin" isomarkitdownplug semanticChunker 500:30

#For ISO20022 Material marker
uv run .\RAG\chunk.py "${basedir}\\outputs\\marker" marker markdownHeaderTextSplitter 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\marker" marker unstructuredMarkdownLoaderSingle 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\marker" marker unstructuredMarkdownLoaderElements 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\marker" marker semanticChunker 500:30

#For ISO20022 Web / Business
uv run .\RAG\chunk.py "${basedir}\\outputs\\iso20022org" iso20022org markdownHeaderTextSplitter 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\iso20022org" iso20022org unstructuredMarkdownLoaderSingle 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\iso20022org" iso20022org unstructuredMarkdownLoaderElements 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\iso20022org" iso20022org semanticChunker 500:30

#For EventCatalog
uv run .\RAG\chunk.py "${basedir}\\outputs\\eventcatalog" eventcatalog markdownHeaderTextSplitter 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\eventcatalog" eventcatalog unstructuredMarkdownLoaderSingle 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\eventcatalog" eventcatalog unstructuredMarkdownLoaderElements 500:30
uv run .\RAG\chunk.py "${basedir}\\outputs\\eventcatalog" eventcatalog semanticChunker 500:30

```


#uv run .\RAG\chunk.py 'E:\\AI\\DocVec\\outputs\\markitdown_plugin\\' pain_markit semanticChunker 0:30


# TODO's:
- [ ] Migrate from local storage to S3 bucket 