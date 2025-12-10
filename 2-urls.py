import json
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def extract_date_of_birth(date_str):
    parts = date_str.split('/')
    if len(parts) == 3:
        month = parts[0]
        day = parts[1]
        year = parts[2]
        return month, day, year
    else:
        return '', '', ''

# Caminho para o arquivo JSON com as URLs das atrizes
input_file = "resultados/urls-atrizes.json"
output_errors_file = "resultados/erros.json"

# Carregar os dados do arquivo JSON e contar o número total de atrizes
with open(input_file, 'r', encoding='utf-8') as f:
    actresses_data = json.load(f)

total_actresses = len(actresses_data)
print(f"Total de atrizes disponíveis para coleta: {total_actresses}")

def save_actress_data(actress_info):
    filename = f"{actress_info['id']}-{actress_info['nome']}.json"
    filepath = os.path.join("atrizes", filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(actress_info, f, ensure_ascii=False, indent=4)

def collect_actresses_data(start_id, num_actresses):
    filtered_actresses = [actress for actress in actresses_data if actress['id'] >= start_id]
    actresses_to_collect = filtered_actresses[:num_actresses]

    with tqdm(total=len(actresses_to_collect), position=0, leave=True) as pbar:
        error_actresses = []  # Lista para armazenar atrizes que deram erro
        for actress in actresses_to_collect:
            if 'url_bio' not in actress:
                print(f"Erro: Chave 'url' ausente para a atriz {actress['nome']}")
                continue

            actress_url = actress['url_bio']
            pbar.set_description(f"Coletando dados para: {actress['nome']}")

            try:
                response = requests.get(actress_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')

                    actress_info = {
                        'id': actress['id'],
                        'actressUrl': actress_url,
                        'url-amigavel': actress['url_bio'],
                        'nome': actress['nome'],
                        'imagem': soup.select_one('div.dashboard-image-container > a > img')['src'] if soup.select_one('div.dashboard-image-container > a > img') else '',
                        'apelidos': ', '.join(apelido.text.strip() for apelido in soup.select('[data-test="link_span_aliases"]')),
                        'data_nascimento': soup.select_one('span[data-test="link_span_dateOfBirth"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_dateOfBirth"]') else '',
                        'data_morte': soup.select_one('span[data-test="link_span_died_on"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_died_on"]') else '',
                        'signo': soup.select_one('span[data-test="link_span_zodiac"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_zodiac"]') else '',
                        'etnia': soup.select_one('span[data-test="link_span_ethnicity"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_ethnicity"]') else '',
                        'altura': soup.select_one('span[data-test="link_span_height"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_height"]') else '',
                        'peso': soup.select_one('span[data-test="link_span_weight"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_weight"]') else '',
                        'cor_cabelo': soup.select_one('span[data-test="link_span_hair_color"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_hair_color"]') else '',
                        'cor_olhos': soup.select_one('span[data-test="link_span_eye_color"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_eye_color"]') else '',
                        'piercings': soup.select_one('span[data-test="link_span_piercings"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_piercings"]') else '',
                        'tattoos': soup.select_one('span[data-test="link_span_tattoos"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_tattoos"]') else '',
                        'pes': soup.select_one('span[data-test="link_span_shoe_size"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_shoe_size"]') else '',
                        'pais_nascimento': soup.select_one('div.flex.self-center > div:nth-child(3) > div > a')['aria-label'] if soup.select_one('div.flex.self-center > div:nth-child(3) > div > a') else '',
                        'profissao': soup.select_one('span[data-test="link_span_profession"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_profession"]') else '',
                        'status': soup.select_one('span[data-test="link_span_careerStatus"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_careerStatus"]') else '',
                        'sexualidade': soup.select_one('span[data-test="link_span_sexualOrientation"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_sexualOrientation"]') else '',
                        'seios': soup.select_one('span[data-test="link_span_boobs"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_boobs"]') else '',
                        'quadril': soup.select_one('span[data-test="link_span_butt"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_butt"]') else '',
                        'nacionalidade': soup.select_one('span[data-test="link_span_nationality"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_nationality"]') else '',
                        'medidas_seios': soup.select_one('span[data-test="link_span_bust"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_bust"]') else '',
                        'tamanho_sutia': soup.select_one('span[data-test="link_span_cup"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_cup"]') else '',
                        'comeco_carreira': soup.select_one('span[data-test="link_span_careerStart"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_careerStart"]') else '',
                        'fim_carreira': soup.select_one('span[data-test="link_span_careerEnd"]').get_text(strip=True) if soup.select_one('span[data-test="link_span_careerEnd"]') else '',
                    }

                    links_container = soup.select_one("#search-result > section > form > div.profile-meta-item.block-shadow.inline-edit-form__partial.inline-edit-form__partial--nobutton.js-inline-edit-form-partial > div.mb-2.md\\:mb-4.grid-scroll.js-grid-scroll > div")
                    if links_container:
                        links = links_container.find_all('a', class_='teaser__link')
                        links_list = [link['href'] for link in links]
                        actress_info['teaser_links'] = links_list

                    save_actress_data(actress_info)
                else:
                    print(f"Erro HTTP {response.status_code} ao acessar {actress_url}")
                    error_actresses.append({
                        'id': actress['id'],
                        'nome': actress['nome'],
                        'url': actress_url
                    })

            except Exception as e:
                print(f"Erro ao coletar dados para {actress['nome']}: {str(e)}")
                error_actresses.append({
                    'id': actress['id'],
                    'nome': actress['nome'],
                    'url': actress_url,
                    'erro': str(e)
                })

            pbar.update(1)

        with open(output_errors_file, 'w', encoding='utf-8') as error_file:
            json.dump(error_actresses, error_file, ensure_ascii=False, indent=4)

        if error_actresses:
            print("\nAtrizes que deram erro durante a coleta:")
            for actress_error in error_actresses:
                print(f"- ID: {actress_error['id']}, Nome: {actress_error['nome']}, URL: {actress_error['url']}")

if __name__ == "__main__":
    try:
        start_id = int(input("A partir de qual ID deseja começar a coleta? "))
        num_actresses = int(input("Quantas atrizes deseja coletar? "))
    except ValueError:
        print("Entrada inválida. Utilizando valores padrão.")
        start_id = 1
        num_actresses = 5

    os.makedirs("atrizes", exist_ok=True)

    collect_actresses_data(start_id, num_actresses)
