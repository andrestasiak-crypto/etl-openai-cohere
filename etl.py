import os
import json
import pandas as pd
import random
from dotenv import load_dotenv
from openai import OpenAI
import openai
import cohere

# 1) Configuração
load_dotenv()
client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client_cohere = cohere.Client(os.getenv("COHERE_API_KEY"))

# Mensagens offline (fallback final)
OFFLINE_MESSAGES = [
    "Investir é a chave para o futuro financeiro!",
    "Faça seu dinheiro trabalhar por você.",
    "Invista hoje e conquiste estabilidade amanhã.",
    "Não deixe sua grana parada, faça ela crescer!",
    "Diversifique seus investimentos para reduzir riscos.",
    "O futuro financeiro começa com decisões inteligentes hoje.",
    "Cada investimento é um passo rumo à liberdade financeira.",
    "Invista regularmente e veja seu patrimônio crescer.",
    "Não espere: comece a investir agora e colha os frutos amanhã.",
    "Investir é plantar hoje para colher prosperidade no futuro."
]

# Modelos OpenAI
GPT_MODELS = [
    "gpt-3.5-turbo",
    "gpt-5-chat-latest",
    "gpt-5-2025-08-07",
    "gpt-5",
    "gpt-4o"
]

# 2) Extract
def extract_users(csv_path: str) -> list[dict]:
    df = pd.read_csv(csv_path)
    users = df.to_dict(orient="records")
    for u in users:
        u["id"] = u.get("UserID", u.get("id"))
        u["news"] = []
    return users

# 3) Transform
def generate_with_openai(name: str) -> str:
    for model in GPT_MODELS:
        completion = None
        try:
            completion = client_openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Você é um especialista em marketing bancário"},
                    {"role": "user", "content": f"Crie uma mensagem curta para {name} sobre investimentos (máx. 100 caracteres)."}
                ],
                temperature=0.7,
            )
            print(f"[Info] Mensagem gerada com {model}")
            if hasattr(completion, "usage"):
                print(">> Tokens consumidos:")
                print("   Prompt:", completion.usage.prompt_tokens)
                print("   Completion:", completion.usage.completion_tokens)
                print("   Total:", completion.usage.total_tokens)
            return completion.choices[0].message.content.strip()
        except openai.RateLimitError as e:
            print(f"[Aviso] Sem quota na OpenAI ({model}). Erro: {e}")
            continue
        except Exception as e:
            print(f"[Aviso] Falha com {model}. Erro: {e}")
            continue
    raise Exception("OpenAI indisponível")

def generate_with_cohere(name: str) -> str:
    try:
        response = client_cohere.chat(
            model="command-a-03-2025",  # modelo atual suportado
            message=f"Crie uma mensagem curta para {name} sobre investimentos(máx. 100 caracteres)."
        )
        print("[Info] Mensagem gerada com Cohere Chat API (command-a-03-2025)")
        return response.text.strip()
    except Exception as e:
        print(f"[Aviso] Falha na Cohere Chat API. Erro: {e}")
        raise

def generate_message_first_user(name: str) -> str:
    try:
        return generate_with_openai(name)
    except Exception:
        try:
            return generate_with_cohere(name)
        except Exception:
            print("[Aviso] Nenhum modelo respondeu. Usando offline.")
            return f"{name}, {random.choice(OFFLINE_MESSAGES)}"

def generate_message_offline(name: str) -> str:
    return f"{name}, {random.choice(OFFLINE_MESSAGES)}"

def transform_users(users: list[dict]) -> list[dict]:
    for idx, user in enumerate(users):
        if idx == 0:
            msg = generate_message_first_user(user["name"])
        else:
            msg = generate_message_offline(user["name"])
        user["news"].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": msg
        })
    return users

# 4) Load
def load_outputs(users: list[dict], json_path: str, csv_path: str) -> None:
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

    flattened = []
    for u in users:
        for n in u.get("news", []):
            flattened.append({
                "id": u.get("id"),
                "name": u.get("name"),
                "description": n.get("description")
            })
    pd.DataFrame(flattened).to_csv(csv_path, index=False)

# 5) Pipeline
def etl_pipeline(csv_input: str, json_output: str, csv_output: str) -> None:
    print(">> Extract")
    users = extract_users(csv_input)
    print(f"Usuários extraídos: {len(users)}")

    print(">> Transform")
    users = transform_users(users)
    print("Mensagens geradas.")

    print(">> Load")
    load_outputs(users, json_output, csv_output)
    print(f"Arquivos salvos: {json_output} e {csv_output}")

if __name__ == "__main__":
    etl_pipeline(
        csv_input="SDW2023.csv",
        json_output="users_news.json",
        csv_output="users_news.csv"
    )
