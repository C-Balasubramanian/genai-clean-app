# # from openai import AzureOpenAI
# # from app.config import *

# # client = AzureOpenAI(
# #     api_key=AZURE_OPENAI_KEY,
# #     azure_endpoint=AZURE_OPENAI_ENDPOINT,
# #     api_version=AZURE_API_VERSION,
# # )

# # def ask_ai(message: str):
# #     res = client.chat.completions.create(
# #         model=AZURE_OPENAI_DEPLOYMENT,
# #         messages=[
# #             {"role": "user", "content": message}
# #         ]
# #     )
# #     return res.choices[0].message.content

# from groq import Groq
# from app.config import GROQ_API_KEY, GROQ_MODEL

# client = Groq(api_key=GROQ_API_KEY)

# def ask_ai(message: str):
#     response = client.chat.completions.create(
#         model=GROQ_MODEL,
#         messages=[{"role": "user", "content": message}]
#     )
#     return response.choices[0].message.content



from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL

_client = None

def get_client():
    global _client
    if _client is None:
        _client = Groq(api_key=GROQ_API_KEY)
    return _client


def ask_ai(message: str) -> str:
    client = get_client()

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    )

    return response.choices[0].message.content
