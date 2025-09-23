import os

from collections.abc import AsyncIterable
from typing import Any, Literal

import httpx

from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel
from typing import Annotated, TypedDict
from langchain_ollama import OllamaEmbeddings
# from langgraph import StateGraph, tool, ToolNode, ToolMessage
from langchain_qdrant import QdrantVectorStore
import os
from  langchain_core.tools.retriever import create_retriever_tool
from os.path import join, dirname
from dotenv import load_dotenv
import qdrant_client
memory = MemorySaver()
dotenv_path = join(dirname(__file__), '../.env')

load_dotenv(dotenv_path)

embeddings_model = os.getenv('EMBEDDINGS_MODEL')
# class State(TypedDict):
#     messages: Annotated[list, add_messages]
client = qdrant_client.QdrantClient(
    os.getenv('QDRANT_API'),
    # api_key=os.getenv('QDRANT_KEY'),, # For Qdrant Cloud, None for local instance
    api_key="<qdrant-api-key>", # For Qdrant Cloud, None for local instance
)



def create_retriever(collection_name):
    vector_store = QdrantVectorStore(client=client, collection_name=collection_name,embedding=OllamaEmbeddings(model=embeddings_model))
    return vector_store.as_retriever()

isoorg_retriver_tool = create_retriever_tool(
    # create_retriever("ISO20022ORG"),
    create_retriever("marker_markdownHeaderTextSplitter"),
    "retriever_iso20022org_mdr",
    "Search and return information about ISO20022 documents and their MDR (Message Definition Report), it messages specification from all domains.",
)

isobusiness_retriever_tool = create_retriever_tool(
    # create_retriever("ISO20022WEB_GENERAL"),
    create_retriever("iso20022org_markdownHeaderTextSplitter"),
    "retriever_iso20022_general",
    "Search and return information about business impact of ISO20022 / CBPR+ changes.",
)

techdoc_retriever_tool = create_retriever_tool(
    # create_retriever("ISO20022_SYSTEM_DOCS"),
    create_retriever("eventcatalog_markdownHeaderTextSplitter"),
    "retriever_system_docs",
    "Search and return documentation of ordering system",
)

@tool
def get_exchange_rate(
    currency_from: str = 'USD',
    currency_to: str = 'EUR',
    currency_date: str = 'latest',
):
    """Use this to get current exchange rate.

    Args:
        currency_from: The currency to convert from (e.g., "USD").
        currency_to: The currency to convert to (e.g., "EUR").
        currency_date: The date for the exchange rate or "latest". Defaults to
            "latest".

    Returns:
        A dictionary containing the exchange rate data, or an error message if
        the request fails.
    """
    try:
        response = httpx.get(
            f'https://api.frankfurter.app/{currency_date}',
            params={'from': currency_from, 'to': currency_to},
        )
        response.raise_for_status()

        data = response.json()
        if 'rates' not in data:
            return {'error': 'Invalid API response format.'}
        return data
    except httpx.HTTPError as e:
        return {'error': f'API request failed: {e}'}
    except ValueError:
        return {'error': 'Invalid JSON response from API.'}

@tool
def retrive_document(
    document:str="example document?",
):
    """Use this to get current exchange rate2.

    Args:
        currency_from: The currency to convert from (e.g., "USD").
        currency_to: The currency to convert to (e.g., "EUR").
        currency_date: The date for the exchange rate or "latest". Defaults to
            "latest".

    Returns:
        A dictionary containing the exchange rate data, or an error message if
        the request fails.
    """
    try:
        response = httpx.get(
            f'https://api.frankfurter.app/{currency_date}',
            params={'from': currency_from, 'to': currency_to},
        )
        response.raise_for_status()

        data = response.json()
        if 'rates' not in data:
            return {'error': 'Invalid API response format.'}
        return data
    except httpx.HTTPError as e:
        return {'error': f'API request failed: {e}'}
    except ValueError:
        return {'error': 'Invalid JSON response from API.'}


class ResponseFormat(BaseModel):
    """Respond to the user in this format."""

    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str


class AnalystAgent:
    """AnalystAgent - a specialized assistant for analytical convesions."""

    SYSTEM_INSTRUCTION = (
        'You are a specialized assistant for currency conversions. '
        # "Your sole purpose is to use the 'get_exchange_rate' tool to answer questions about currency exchange rates. "
        "Your sole purpose is to use the following tools to answer questions:"
        " get_exchange_rate  - about currency exchange rates. "
        " isoorg_retriver_tool  - about ISO20022 specification . "
        " isobusiness_retriever_tool  - about ISO20022 business changes and impact. "
        " techdoc_retriever_tool  - about ordering system specification. "
        'If the user asks about anything other than: currency exchange rates conversion ISO20022 specification,  ISO20022 business changes and impact,  ordering system specification or exchange rates, '
        'politely state that you cannot help with that topic and can only assist with provided topics. '
        'Do not attempt to answer unrelated questions or use tools for other purposes.'
    )

    FORMAT_INSTRUCTION = (
        'Set response status to input_required if the user needs to provide more information to complete the request.'
        'Set response status to error if there is an error while processing the request.'
        'Set response status to completed if the request is complete.'
    )

    def __init__(self):
        model_source = os.getenv('model_source', 'google')
        if model_source == 'google':
            self.model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
        else:
            self.model = ChatOpenAI(
                model=os.getenv('TOOL_LLM_NAME'),
                openai_api_key=os.getenv('API_KEY', 'EMPTY'),
                openai_api_base=os.getenv('TOOL_LLM_URL'),
                temperature=0,
            )
        # tools = [hf_retriever_tool, transformer_retriever_tool, search_tool]
        self.tools = [get_exchange_rate,isoorg_retriver_tool,isobusiness_retriever_tool,techdoc_retriever_tool]

        self.graph = create_react_agent(
            self.model,
            tools=self.tools,
            checkpointer=memory,
            prompt=self.SYSTEM_INSTRUCTION,
            response_format=(self.FORMAT_INSTRUCTION, ResponseFormat),
        )

    async def stream(self, query, context_id) -> AsyncIterable[dict[str, Any]]:
        inputs = {'messages': [('user', query)]}
        config = {'configurable': {'thread_id': context_id}}

        for item in self.graph.stream(inputs, config, stream_mode='values'):
            message = item['messages'][-1]
            if (
                isinstance(message, AIMessage)
                and message.tool_calls
                and len(message.tool_calls) > 0
            ):
                yield {
                    'is_task_complete': False,
                    'require_user_input': False,
                    'content': 'Looking up the data...',
                }
            elif isinstance(message, ToolMessage):
                yield {
                    'is_task_complete': False,
                    'require_user_input': False,
                    'content': 'Processing the data..',
                }

        yield self.get_agent_response(config)

    def get_agent_response(self, config):
        current_state = self.graph.get_state(config)
        structured_response = current_state.values.get('structured_response')
        if structured_response and isinstance(
            structured_response, ResponseFormat
        ):
            if structured_response.status == 'input_required':
                return {
                    'is_task_complete': False,
                    'require_user_input': True,
                    'content': structured_response.message,
                }
            if structured_response.status == 'error':
                return {
                    'is_task_complete': False,
                    'require_user_input': True,
                    'content': structured_response.message,
                }
            if structured_response.status == 'completed':
                return {
                    'is_task_complete': True,
                    'require_user_input': False,
                    'content': structured_response.message,
                }

        return {
            'is_task_complete': False,
            'require_user_input': True,
            'content': (
                'We are unable to process your request at the moment. '
                'Please try again.'
            ),
        }

    SUPPORTED_CONTENT_TYPES = ['text', 'text/plain']
