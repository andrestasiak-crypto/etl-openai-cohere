# Guia de Uso

1. Configure suas chaves no `.env` (baseado no `.env.example`).
2. Execute `etl.py`.
3. Verifique os arquivos de saída:
   - `users_news.json`
   - `users_news.csv`

---

## Saída no terminal

- Tokens consumidos (quando OpenAI responde).
- Mensagens de fallback (quando OpenAI/Cohere falham).
- Logs informativos sobre cada etapa do ETL.

---

## Exemplo

```bash
>> Extract
Usuários extraídos: 5

>> Transform
[Info] Mensagem gerada com gpt-3.5-turbo
>> Tokens consumidos:
   Prompt: 25
   Completion: 12
   Total: 37

[Aviso] Sem quota na OpenAI (gpt-3.5-turbo). Erro: RateLimitError
[Info] Mensagem gerada com Cohere Chat API (command-light)

>> Load
Arquivos salvos: users_news.json e users_news.csv
