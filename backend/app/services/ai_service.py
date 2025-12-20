# from openai import AzureOpenAI
# from app.config import *

# client = AzureOpenAI(
#     api_key=AZURE_OPENAI_KEY,
#     azure_endpoint=AZURE_OPENAI_ENDPOINT,
#     api_version=AZURE_API_VERSION,
# )

# def ask_ai(message: str):
#     res = client.chat.completions.create(
#         model=AZURE_OPENAI_DEPLOYMENT,
#         messages=[
#             {"role": "user", "content": message}
#         ]
#     )
#     return res.choices[0].message.content

from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def ask_ai(message: str):
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content


