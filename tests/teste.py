from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega a chave do .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1) Lista de modelos disponíveis
models = client.models.list()
print("Modelos disponíveis na sua conta:")
for m in models.data[:10]:  # mostra só os 10 primeiros
    print("-", m.id)

# 2) Faz uma chamada simples de teste
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # escolha um modelo que apareceu na lista
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Teste rápido: diga Olá em português."}
    ]
)

print("Resposta do modelo:", completion.choices[0].message.content)

# 3) Mostra consumo de tokens
if hasattr(completion, "usage"):
    print(">> Tokens consumidos:")
    print("   Prompt:", completion.usage.prompt_tokens)
    print("   Completion:", completion.usage.completion_tokens)
    print("   Total:", completion.usage.total_tokens)