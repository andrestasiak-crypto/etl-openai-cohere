# ETL OpenAI + Cohere 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&logoColor=white)

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

```

## 📊 Resultado esperado

Ao rodar o pipeline ETL, você deve ver no terminal mensagens indicando cada etapa (**Extract → Transform → Load**) e os arquivos de saída gerados (`users_news.json` e `users_news.csv`).

### Exemplo de execução

<img width="1325" height="980" alt="image" src="https://github.com/user-attachments/assets/284de9b5-a981-4594-b344-8a5e9c3f036c" />

> A imagem acima mostra um exemplo de execução do ETL com mensagens geradas pela OpenAI, fallback para Cohere e saída final salva em JSON/CSV.

## 👨‍💻 Autor

**André Stasiak**

- 💼 [LinkedIn](https://www.linkedin.com/in/andre-stasiak)  
- 💻 [GitHub](https://github.com/andrestasiak-crypto)  
- 📧 Email: andrestasiak@gmail.com  

Apaixonado por tecnologia, dados e inteligência artificial.  
Este projeto foi desenvolvido como parte do desafio **Santander Dev Week**, integrando **OpenAI** e adicionado o **Cohere** em um pipeline ETL resiliente e escalável.

