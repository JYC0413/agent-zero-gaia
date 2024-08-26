from langchain_openai import ChatOpenAI

import models


def perplexity_search(query: str, api_key=None,
                      base_url="https://codestral.us.gaianet.network/v1", model_name="codestral"):
    api_key = api_key or models.get_api_key("perplexity")

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