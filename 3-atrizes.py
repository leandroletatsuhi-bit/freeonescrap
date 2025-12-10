import json
import os
from urllib.parse import urlparse
from datetime import datetime  # Adicionando importação do datetime

def parse_date(date_str):
    # Parse da string de data no formato adequado
    try:
        # Remover parte extra (como " At The Age Of 31") se presente
        date_str = date_str.split(" At")[0].strip()
        # Parse da data
        date = datetime.strptime(date_str, "%B %d, %Y")
        # Extrair o mês, dia e ano
        month = date.strftime("%B")  # Nome do mês completo
        day = date.strftime("%d")  # Dia
        year = date.strftime("%Y")  # Ano
        return month, day, year
    except ValueError:
        return None, None, None  # Em caso de erro, retorna None para todos

def get_domain(url):
    # Extrair o domínio da URL
    parsed_url = urlparse(url)
    return parsed_url.netloc

def merge_actresses_data():
    # Lista para armazenar os dados de todas as atrizes
    all_actresses_data = []

    # Percorrer os arquivos de atrizes na pasta "atrizes"
    actresses_folder = "atrizes"
    for filename in os.listdir(actresses_folder):
        if filename.endswith(".json"):
            filepath = os.path.join(actresses_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                actress_info = json.load(f)
                # Processar a data de nascimento, se presente
                if "data_nascimento" in actress_info:
                    month, day, year = parse_date(actress_info["data_nascimento"])
                    if month is not None and day is not None and year is not None:
                        actress_info["mes_nascimento"] = month
                        actress_info["dia_nascimento"] = day
                        actress_info["ano_nascimento"] = year
                # Processar a data de morte, se presente
                if "data_morte" in actress_info:
                    month, day, year = parse_date(actress_info["data_morte"])
                    if month is not None and day is not None and year is not None:
                        actress_info["mes_morte"] = month
                        actress_info["dia_morte"] = day
                        actress_info["ano_morte"] = year
                # Processar os links externos
                if "teaser_links" in actress_info and isinstance(actress_info["teaser_links"], list):
                    link_info = {}
                    for link in actress_info["teaser_links"]:
                        domain = get_domain(link)
                        if domain not in link_info:
                            link_info[domain] = []
                        link_info[domain].append(link)
                    actress_info["teaser_links_info"] = link_info
                # Remover a chave "teaser_links" se necessário
                # if "teaser_links" in actress_info:
                #     del actress_info["teaser_links"]
                all_actresses_data.append(actress_info)

    # Ordenar os dados das atrizes por ID em ordem crescente
    all_actresses_data.sort(key=lambda x: x.get('id', 0))

    # Caminho para o arquivo de saída contendo todos os dados das atrizes
    output_file = "resultados/atrizes.json"

    # Salvar os dados de todas as atrizes em um único arquivo JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_actresses_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Chamar a função para mesclar e organizar os dados de todas as atrizes
    merge_actresses_data()

    print("Dados de todas as atrizes foram organizados por ID em ordem crescente e salvos em 'resultados/atrizes.json'.")
