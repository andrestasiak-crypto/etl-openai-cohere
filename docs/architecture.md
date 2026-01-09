# Arquitetura do ETL

O pipeline segue o padrão **Extract → Transform → Load**:

1. **Extract**  
   - Lê usuários de um arquivo CSV (`SDW2023.csv`).

2. **Transform**  
   - Para o primeiro usuário: tenta gerar mensagem com OpenAI.  
   - Se falhar: tenta Cohere (`command-light`).  
   - Se também falhar: usa mensagens offline.  
   - Para os demais usuários: mensagens offline direto.

3. **Load**  
   - Exporta resultados para `users_news.json` e `users_news.csv`.

---

## Fluxo resumido

---

## Destaques técnicos
- **Fallback inteligente**: garante que o pipeline nunca quebra.  
- **Mensagens personalizadas**: simulam marketing bancário real.  
- **Resiliência**: mesmo sem quota de API, o sistema gera saída offline.


