from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega a chave do arquivo .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Lista todos os modelos disponíveis na sua conta
models = client.models.list()

for m in models.data:
    print(m.id)
