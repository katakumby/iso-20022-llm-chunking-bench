# Setup langflow

... generate api keys and place them in agent env's

## On-prem
```bash
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up

```
## Cloud

Open https://langfuse.com/ and setup account

# Run Qdrant
Locally: https://qdrant.tech/documentation/quickstart/

## Prepare data for qdrant

Check [README.md](analyst-langgraph/RAG/README.md)

## S3

Sync docs: ```aws s3 sync .\outputs s3://amzn-s3-agents-sources/```

# A2A Inspector

Follow: https://github.com/a2aproject/a2a-inspector 

UI: http://127.0.0.1:5001/

# Run vLLM

Embeddings:
```bash
docker run --runtime nvidia --gpus all -v E:\AI\models:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=YOUR_TOKEN" -p 8000:8000 --ipc=host  vllm/vllm-openai:latest --model Qwen/Qwen3-Embedding-8B --task embed --host 0.0.0.0 --port 8000
```

LLM (with tools):
```bash
docker run --runtime nvidia --gpus all -v E:\AI\models:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=YOUR_TOKEN" -p 8000:8000 --ipc=host  vllm/vllm-openai:latest --model Qwen/Qwen3-Coder-30B-A3B-Instruct --enable-auto-tool-choice --tool-call-parser llama3_json
```

# Run Agent(s)

Check [README.md](analyst-langgraph/README.md)

# Agents Coordinator

Some google project, it worked, im searching what was that, smth local with hardcoded google llms :) 