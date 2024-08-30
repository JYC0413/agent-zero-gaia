import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import models

load_dotenv()


def perplexity_search(query: str, api_key=None, model_name=None, base_url=None):
    perplexityKey = models.get_api_key("perplexity")
    if perplexityKey:
        api_key = models.get_api_key("perplexity")
        model_name = "llama-3.1-sonar-large-128k-online"
        base_url = "https://api.perplexity.ai"
    else:
        api_key = api_key or os.getenv("CHAT_API_KEY") or "LLAMAEDGE"
        model_name = model_name or os.getenv("CHAT_MODEL_NAME") or "llama"
        base_url = base_url or os.getenv("CHAT_MODEL_BASE_URL") or "https://llama.us.gaianet.network/v1"

    client = ChatOpenAI(api_key=api_key, model=model_name, base_url=base_url)

    messages = [
        # It is recommended to use only single-turn conversations and avoid system prompts for the online LLMs (sonar-small-online and sonar-medium-online).

        # {
        #     "role": "system",
        #     "content": (
        #         "You are an artificial intelligence assistant and you need to "
        #         "engage in a helpful, detailed, polite conversation with a user."
        #     ),
        # },
        {
            "role": "user",
            "content": (
                query
            ),
        },
    ]

    response = client.invoke(messages)
    result = response.content  # only the text is returned
    print(result)
    return result
