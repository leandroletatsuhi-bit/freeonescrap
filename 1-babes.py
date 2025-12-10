import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urljoin
from pathlib import Path
import time
import random
import re  # Para regex na classe

def scrape_babes_pages(max_page):
    base_url = "https://www.freeones.com/performers?f%5BperformerType%5D=babe&s=rank.currentRank&o=asc&l=24&m%5BmeasurementSystem%5D=metric&p={}"

    output_dir = Path("resultados")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "urls-atrizes.json"

    atrizes_data = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    with tqdm(total=max_page, desc="Coletando páginas") as pbar:
        for page_num in range(1, max_page + 1):
            try:
                url = base_url.format(page_num)
                response = requests.get(url, headers=headers, timeout=15)

                if response.status_code != 200:
                    print(f"Falha na página {page_num}: status {response.status_code}")
                    pbar.update(1)
                    time.sleep(random.uniform(3, 6))
                    continue

                soup = BeautifulSoup(response.content, 'html.parser')

                # Busca <a> com class contendo "teaser__link" (regex para ignorar espaço inicial)
                atrizes_links = soup.find_all('a', class_=re.compile(r'teaser__link'))

                if not atrizes_links:
                    print(f"Nenhum teaser__link encontrado na página {page_num}. Site mudou de novo?")
                    break

                print(f"Página {page_num}: {len(atrizes_links)} atrizes encontradas.")

                for link in atrizes_links:
                    href = link.get('href')
                    if not href or '/feed' not in href:
                        continue  # Ignora se não for feed

                    atriz_url_feed = urljoin("https://www.freeones.com", href)
                    atriz_url_bio = atriz_url_feed.replace('/feed', '/bio')

                    # Nome preciso: p com data-test="subject-name"
                    nome_tag = link.find('p', attrs={'data-test': 'subject-name'})
                    atriz_nome = nome_tag.get_text(strip=True) if nome_tag else "Nome não encontrado"

                    # Slug: do path, removendo /bio ou /feed
                    path = href.strip('/')
                    slug = path.rsplit('/', 1)[0] if '/' in path else path

                    atriz_data = {
                        "id": len(atrizes_data) + 1,
                        "url_bio": atriz_url_bio,
                        "url_feed": atriz_url_feed,
                        "nome": atriz_nome,
                        "slug": slug
                    }
                    atrizes_data.append(atriz_data)

                pbar.update(1)
                time.sleep(random.uniform(2, 5))  # Humano

            except Exception as e:
                print(f"Erro na página {page_num}: {str(e)}")
                pbar.update(1)
                time.sleep(random.uniform(5, 10))

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(atrizes_data, f, ensure_ascii=False, indent=4)

    print(f"\nFinalizado: {len(atrizes_data)} atrizes coletadas.")
    print(f"Salvo em {output_file}")

if __name__ == "__main__":
    try:
        max_page = int(input("Até qual página deseja coletar? (ex: 10): "))
    except ValueError:
        max_page = 5
        print("Inválido, usando 5.")

    scrape_babes_pages(max_page)