# ETL OpenAI + Cohere 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

Pipeline **ETL** desenvolvido para o desafio **Santander Dev Week**, utilizando a API da **OpenAI** para gerar mensagens de marketing personalizadas.  
Inclui **fallback automático** para **Cohere (command-light)** e, caso nenhuma IA responda, mensagens **offline simuladas**.

---

## ⚙️ Tecnologias
- Python 3.13
- OpenAI API
- Cohere Chat API (`command-light`)
- Pandas
- Dotenv

---

## 📂 Estrutura
- `etl.py` → código principal do ETL
- `SDW2023.csv` → exemplo de entrada com usuários
- `users_news.json` / `users_news.csv` → saída gerada (não versionada, apenas local)
- `.env.example` → exemplo de configuração das chaves
- `.gitignore` → protege segredos e arquivos temporários
- `docs/` → documentação extra
- `tests/` → scripts de teste e rascunhos

---

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/andrestasiak-crypto/etl-openai-cohere.git
cd etl-openai-cohere

# Crie o ambiente virtual
python -m venv venv
source venv/Scripts/activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Configure suas chaves
cp .env.example .env
# edite o arquivo .env e coloque:
# OPENAI_API_KEY=sk-xxxx
# COHERE_API_KEY=xxxx

# Execute
python etl.py
