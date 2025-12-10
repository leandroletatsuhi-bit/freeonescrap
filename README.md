# FreeOnes Scraper: Banco de Dados Automático de Perfis Adultos

Este projeto é uma ferramenta poderosa e automatizada para coletar dados de perfis de atrizes do site FreeOnes.com. Ele raspa listas de "babes" (páginas de ranking), extrai URLs de bios e depois puxa detalhes ricos: medidas, etnia, altura, nacionalidade, links para OnlyFans/Instagram/Twitter e mais. Tudo salvo em JSONs limpos, atualizados diariamente via GitHub Actions.

**Por que isso importa?**  
Em um mundo de conteúdo adulto bilionário, dados são ouro. Use para análise de tendências, marketing afiliado, funis de OnlyFans ou até venda de leads premium. Mas lembre: respeite leis (GDPR, TOS do site) — anonimze e agregue para ética.

## Funcionalidades Principais
- **Coleta Inicial (1-babes.py)**: Raspa até N páginas de ranking (24 perfis/página), extrai nomes, slugs e URLs de bio/feed.
- **Coleta Detalhada (2-urls.py)**: Entra em cada bio, puxa atributos chave (altura, peso, signo, social links) e salva JSON individual.
- **Automação Total**: GitHub Actions roda diariamente (50 páginas novas + bios), commita updates no repo.
- **Robustez**: Delays randômicos, timeouts, headers humanos — evita bans.
- **Saída**: 
  - `resultados/urls-atrizes.json`: Lista completa.
  - Pasta `atrizes/`: JSONs por atriz (ex: `1-Willow_Ryder.json`).

Exemplo de output em bio:
```json
{
  "id": 1,
  "nome": "Willow Ryder",
  "url_bio": "https://www.freeones.com/willow-ryder/bio",
  "imagem": "https://thumbs.freeones.com/...",
  "altura": "5'4\"",
  "nacionalidade": "American",
  "social_links": {
    "onlyfans": "https://onlyfans.com/willowryder",
    "instagram": "https://instagram.com/willowryder"
  }
}
