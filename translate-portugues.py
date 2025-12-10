import json

# Dicionários de tradução para cada campo específico

traducoes_tamanho_sutia = {
    "Unknown": "",
}

traducoes_quadril = {
    "Unknown": "",
    "Fake" : "Silicone",
    "Natural": "Naturais",}

traducoes_seios = {
    "Unknown": "",
    "Fake" : "Silicone",
    "Natural": "Naturais",
}

traducoes_sexualidade = {
    "Unknown": "",
    "Bi-Sexual": "Bi-Sexual",
    "Straight": "Hétero",
    "Lesbian": "Lésbica",
    "Gay": "Gay",
    "Pansexual": "Pansexual",
}

traducoes_status = {
    "Unknown": "",
    "Active": "Ativa",
    "Retired": "Aposentada",
    "Deceased": "Falecida",
}

traducoes_profissoes = {
    "Unknown": "",
    "Adult Model": "Modelo Adulta",
    "Porn Star": "Atriz Pornô",
    "Centerfold": "Capa de Revista",
    "Actress": "Atriz",
    "Musician": "Musicista",
    "Celebrities": "Famosas",
    "Sportswoman": "Atletas",
    "TV Host": "Apresentadora",
}

traducoes_signos = {
    "Unknown": "",
    "Aries": "Áries",
    "Taurus": "Touro",
    "Gemini": "Gêmeos",
    "Cancer": "Câncer",
    "Leo": "Leão",
    "Virgo": "Virgem",
    "Libra": "Libra",
    "Scorpio": "Escorpião",
    "Sagittarius": "Sagitário",
    "Capricorn": "Capricórnio",
    "Aquarius": "Aquário",
    "Pisces": "Peixes",
}

traducoes_mes_nascimento = {
    "Unknown": "",
    "January": "Janeiro",
    "February": "Fevereiro",
    "March": "Março",
    "April": "Abril",
    "May": "Maio",
    "June": "Junho",
    "July": "Julho",
    "August": "Agosto",
    "September": "Setembro",
    "October": "Outubro",
    "November": "Novembro",
    "December": "Dezembro",
}

traducoes_mes_morte = {
    "Unknown": "",
    "January": "Janeiro",
    "February": "Fevereiro",
    "March": "Março",
    "April": "Abril",
    "May": "Maio",
    "June": "Junho",
    "July": "Julho",
    "August": "Agosto",
    "September": "Setembro",
    "October": "Outubro",
    "November": "Novembro",
    "December": "Dezembro",
}

traducoes_etnia = {
    "Unknown": "",
    "Asian": "Asiática",
    "Caucasian": "Caucasiana",
    "Latin": "Latina",
    "Black": "Negra",
    "Mixed": "Mestiça",
    "Unknown": "",
}

traducoes_cor_cabelo = {
    "Unknown": "",
    "Black": "Pretos",
    "Brown": "Castanhos",
    "Blonde": "Loiros",
    "Red": "Ruivos",
    # Adicione outras traduções conforme necessário
}

traducoes_cor_olhos = {
    "Unknown": "",
    "Brown": "Castanhos",
    "Blue": "Azuis",
    "Green": "Verdes",
    "Hazel": "Avelã",
    # Adicione outras traduções conforme necessário
}

traducoes_piercings = {
    "Unknown": "",
    "Yes": "Sim",
    "No": "Não",
}

traducoes_tattoos = {
    "Unknown": "",
    "Yes": "Sim",
    "No": "Não",
}

traducoes_pais_nascimento = {
    "Unknown": "",
    "Afghanistan": "Afeganistão",
    "Albania": "Albânia",
    "Algeria": "Argélia",
    "Andorra": "Andorra",
    "Angola": "Angola",
    "Antigua and Barbuda": "Antígua e Barbuda",
    "Argentina": "Argentina",
    "Armenia": "Armênia",
    "Australia": "Austrália",
    "Austria": "Áustria",
    "Azerbaijan": "Azerbaijão",
    "Bahamas": "Bahamas",
    "Bahrain": "Bahrein",
    "Bangladesh": "Bangladesh",
    "Barbados": "Barbados",
    "Belarus": "Bielorrússia",
    "Belgium": "Bélgica",
    "Belize": "Belize",
    "Benin": "Benin",
    "Bhutan": "Butão",
    "Bolivia": "Bolívia",
    "Bosnia and Herzegovina": "Bósnia e Herzegovina",
    "Botswana": "Botsuana",
    "Brazil": "Brasil",
    "Brunei": "Brunei",
    "Bulgaria": "Bulgária",
    "Burkina Faso": "Burkina Faso",
    "Burundi": "Burundi",
    "Cabo Verde": "Cabo Verde",
    "Cambodia": "Camboja",
    "Cameroon": "Camarões",
    "Canada": "Canadá",
    "Central African Republic": "República Centro-Africana",
    "Chad": "Chade",
    "Chile": "Chile",
    "China": "China",
    "Colombia": "Colômbia",
    "Comoros": "Comores",
    "Costa Rica": "Costa Rica",
    "Croatia": "Croácia",
    "Cuba": "Cuba",
    "Cyprus": "Chipre",
    "Czech Republic": "República Tcheca",
    "Denmark": "Dinamarca",
    "Djibouti": "Djibuti",
    "Dominica": "Dominica",
    "Dominican Republic": "República Dominicana",
    "East Timor": "Timor-Leste",
    "Ecuador": "Equador",
    "Egypt": "Egito",
    "El Salvador": "El Salvador",
    "Equatorial Guinea": "Guiné Equatorial",
    "Eritrea": "Eritreia",
    "Estonia": "Estônia",
    "Eswatini": "Eswatini",
    "Ethiopia": "Etiópia",
    "Fiji": "Fiji",
    "Finland": "Finlândia",
    "France": "França",
    "France, Metropolitan": "França",
    "Gabon": "Gabão",
    "Gambia": "Gâmbia",
    "Georgia": "Geórgia",
    "Germany": "Alemanha",
    "Ghana": "Gana",
    "Greece": "Grécia",
    "Grenada": "Granada",
    "Guatemala": "Guatemala",
    "Guinea": "Guiné",
    "Guinea-Bissau": "Guiné-Bissau",
    "Guyana": "Guiana",
    "Haiti": "Haiti",
    "Honduras": "Honduras",
    "Hungary": "Hungria",
    "Iceland": "Islândia",
    "India": "Índia",
    "Indonesia": "Indonésia",
    "Iran": "Irã",
    "Iraq": "Iraque",
    "Ireland": "Irlanda",
    "Israel": "Israel",
    "Italy": "Itália",
    "Ivory Coast": "Costa do Marfim",
    "Jamaica": "Jamaica",
    "Japan": "Japão",
    "Jordan": "Jordânia",
    "Kazakhstan": "Cazaquistão",
    "Kenya": "Quênia",
    "Kiribati": "Kiribati",
    "Kosovo": "Kosovo",
    "Kuwait": "Kuwait",
    "Kyrgyzstan": "Quirguistão",
    "Laos": "Laos",
    "Latvia": "Letônia",
    "Lebanon": "Líbano",
    "Lesotho": "Lesoto",
    "Liberia": "Libéria",
    "Libya": "Líbia",
    "Liechtenstein": "Liechtenstein",
    "Lithuania": "Lituânia",
    "Luxembourg": "Luxemburgo",
    "Madagascar": "Madagáscar",
    "Malawi": "Malawi",
    "Malaysia": "Malásia",
    "Maldives": "Maldivas",
    "Mali": "Mali",
    "Malta": "Malta",
    "Marshall Islands": "Ilhas Marshall",
    "Mauritania": "Mauritânia",
    "Mauritius": "Maurício",
    "Mexico": "México",
    "Micronesia": "Micronésia",
    "Moldova": "Moldávia",
    "Moldova": "República da Moldova",
    "Monaco": "Mônaco",
    "Mongolia": "Mongólia",
    "Montenegro": "Montenegro",
    "Morocco": "Marrocos",
    "Mozambique": "Moçambique",
    "Myanmar": "Myanmar",
    "Namibia": "Namíbia",
    "Nauru": "Nauru",
    "Nepal": "Nepal",
    "Netherlands": "Países Baixos",
    "New Zealand": "Nova Zelândia",
    "Nicaragua": "Nicarágua",
    "Niger": "Níger",
    "Nigeria": "Nigéria",
    "North Korea": "Coreia do Norte",
    "North Macedonia": "Macedônia do Norte",
    "Norway": "Noruega",
    "Oman": "Omã",
    "Pakistan": "Paquistão",
    "Palau": "Palau",
    "Palestine": "Palestina",
    "Panama": "Panamá",
    "Papua New Guinea": "Papua-Nova Guiné",
    "Paraguay": "Paraguai",
    "Peru": "Peru",
    "Philippines": "Filipinas",
    "Poland": "Polônia",
    "Portugal": "Portugal",
    "Puerto Rico": "Porto Rico",
    "Qatar": "Catar",
    "Republic of Moldova": "República da Moldova",
    "Republic of the Congo": "República do Congo",
    "Romania": "Romênia",
    "Russia": "Rússia",
    "Rwanda": "Ruanda",
    "Saint Kitts and Nevis": "São Cristóvão e Névis",
    "Saint Lucia": "Santa Lúcia",
    "Saint Vincent and the Grenadines": "São Vicente e Granadinas",
    "Samoa": "Samoa",
    "San Marino": "San Marino",
    "Sao Tome and Principe": "São Tomé e Príncipe",
    "Saudi Arabia": "Arábia Saudita",
    "Senegal": "Senegal",
    "Serbia": "Sérvia",
    "Seychelles": "Seychelles",
    "Sierra Leone": "Serra Leoa",
    "Singapore": "Singapura",
    "Slovakia": "Eslováquia",
    "Slovenia": "Eslovênia",
    "Solomon Islands": "Ilhas Salomão",
    "Somalia": "Somália",
    "South Africa": "África do Sul",
    "South Korea": "Coreia do Sul",
    "South Sudan": "Sudão do Sul",
    "Spain": "Espanha",
    "Sri Lanka": "Sri Lanka",
    "Sudan": "Sudão",
    "Suriname": "Suriname",
    "Sweden": "Suécia",
    "Switzerland": "Suíça",
    "Syria": "Síria",
    "Syrian Arab Republic": "República Árabe Síria",
    "Taiwan": "Taiwan",
    "Tajikistan": "Tajiquistão",
    "Tanzania": "Tanzânia",
    "Thailand": "Tailândia",
    "Togo": "Togo",
    "Tonga": "Tonga",
    "Trinidad and Tobago": "Trinidad e Tobago",
    "Tunisia": "Tunísia",
    "Turkey": "Turquia",
    "Turkmenistan": "Turcomenistão",
    "Tuvalu": "Tuvalu",
    "Uganda": "Uganda",
    "Ukraine": "Ucrânia",
    "United Arab Emirates": "Emirados Árabes Unidos",
    "United Kingdom": "Reino Unido",
    "United States": "Estados Unidos",
    "Uruguay": "Uruguai",
    "Uzbekistan": "Uzbequistão",
    "Vanuatu": "Vanuatu",
    "Vatican City": "Cidade do Vaticano",
    "Venezuela": "Venezuela",
    "Vietnam": "Vietnã",
    "Yemen": "Iêmen",
    "Zambia": "Zâmbia",
    "Zimbabwe": "Zimbábue",
}

traducoes_nacionalidade = {
    "Unknown": "",
    "Armenian ": "Armeniana",
    "Ukrainian": "Ucraniana",
    "American": "Americana",
    "Afghanistan": "Afegã",
    "Albania": "Albanesa",
    "Algeria": "Argelina",
    "Andorra": "Andorrana",
    "Angola": "Angolana",
    "Antigua and Barbuda": "Antiguana e Barbudense",
    "Argentina": "Argentina",
    "Armenia": "Armênia",
    "Australia": "Australiana",
    "Austria": "Austríaca",
    "Azerbaijan": "Azerbaijana",
    "Bahamas": "Bahamense",
    "Bahrain": "Barenita",
    "Bangladesh": "Bangladeshiana",
    "Barbados": "Barbadiana",
    "Belarus": "Bielorrussa",
    "Belgium": "Belga",
    "Belize": "Belizenha",
    "Benin": "Beninense",
    "Bhutan": "Butanesa",
    "Bolivia": "Boliviana",
    "Bosnia and Herzegovina": "Bósnia",
    "Botswana": "Botsuanesa",
    "Brazil": "Brasileira",
    "Brunei": "Bruneiana",
    "Bulgaria": "Búlgara",
    "Burkina Faso": "Burquinêsa",
    "Burundi": "Burundinêsa",
    "Cabo Verde": "Cabo-verdiana",
    "Cambodia": "Cambojana",
    "Cameroon": "Camaronesa",
    "Canada": "Canadense",
    "Central African Republic": "Centro-africana",
    "Chad": "Chadiana",
    "Chile": "Chilena",
    "China": "Chinesa",
    "Colombia": "Colombiana",
    "Comoros": "Comorense",
    "Democratic Republic of the Congo": "Congolêsa",
    "Republic of the Congo": "Congolêsa",
    "Costa Rica": "Costarriquenha",
    "Croatia": "Croata",
    "Cuba": "Cubana",
    "Cyprus": "Cipriota",
    "Czech Republic": "Tcheca",
    "Denmark": "Dinamarquesa",
    "Djibouti": "Djiboutiana",
    "Dominica": "Dominiquense",
    "Dominican Republic": "Dominicana",
    "East Timor": "Timorense",
    "Ecuador": "Equatoriana",
    "Egypt": "Egípcia",
    "El Salvador": "Salvadorenha",
    "Equatorial Guinea": "Guineense",
    "Eritrea": "Eritreia",
    "Estonia": "Estoniana",
    "Eswatini": "Suazilandesa",
    "Ethiopia": "Etíope",
    "Fiji": "Fijiana",
    "Finland": "Finlandesa",
    "France": "Francesa",
    "French": "Francesa",
    "Gabon": "Gabonesa",
    "Gambia": "Gambiana",
    "Georgia": "Georgiana",
    "Germany": "Alemã",
    "Ghana": "Ganesa",
    "Greece": "Grega",
    "Grenada": "Granadina",
    "Guatemala": "Guatemalteca",
    "Guinea": "Guineana",
    "Guinea-Bissau": "Guineense",
    "Guyana": "Guianense",
    "Haiti": "Haitiana",
    "Honduras": "Hondurenha",
    "Hungary": "Húngara",
    "Iceland": "Islandesa",
    "India": "Indiana",
    "Indonesia": "Indonésia",
    "Iran": "Iraniana",
    "Iraq": "Iraquiana",
    "Ireland": "Irlandesa",
    "Israel": "Israelense",
    "Italy": "Italiana",
    "Ivory Coast": "Costa-marfinense",
    "Jamaica": "Jamaicana",
    "Japan": "Japonesa",
    "Jordan": "Jordaniana",
    "Kazakhstan": "Cazaque",
    "Kenya": "Queniana",
    "Kiribati": "Kiribatiana",
    "Kosovo": "Kosovar",
    "Kuwait": "Kuwaitiana",
    "Kyrgyzstan": "Quirguiz",
    "Laos": "Laosiana",
    "Latvia": "Letona",
    "Lebanon": "Libanesa",
    "Lesotho": "Lesotiana",
    "Liberia": "Liberiana",
    "Libya": "Líbia",
    "Liechtenstein": "Liechtensteiniana",
    "Lithuania": "Lituana",
    "Luxembourg": "Luxemburguesa",
    "Madagascar": "Malgaxe",
    "Malawi": "Malauiana",
    "Malaysia": "Malaia",
    "Maldives": "Maldiviana",
    "Mali": "Maliana",
    "Malta": "Maltesa",
    "Marshall Islands": "Ilhas Marshall",
    "Mauritania": "Mauritana",
    "Mauritius": "Mauriciana",
    "Mexico": "Mexicana",
    "Micronesia": "Micronésia",
    "Moldova": "Moldava",
    "Monaco": "Monegasca",
    "Mongolia": "Mongol",
    "Montenegro": "Montenegrina",
    "Morocco": "Marroquina",
    "Mozambique": "Moçambicana",
    "Myanmar": "Mianmarense",
    "Namibia": "Namibiana",
    "Nauru": "Nauruana",
    "Nepal": "Nepalesa",
    "Netherlands": "Holandesa",
    "New Zealand": "Neozelandesa",
    "Nicaragua": "Nicaraguense",
    "Niger": "Nigeriana",
    "Nigeria": "Nigeriana",
    "North Korea": "Norte-coreana",
    "North Macedonia": "Macedônia do Norte",
    "Norway": "Norueguesa",
    "Oman": "Omanense",
    "Pakistan": "Paquistanesa",
    "Palau": "Palauana",
    "Palestine": "Palestina",
    "Panama": "Panamenha",
    "Papua New Guinea": "Papuásia",
    "Paraguay": "Paraguaia",
    "Peru": "Peruana",
    "Philippines": "Filipina",
    "Poland": "Polonesa",
    "Portugal": "Portuguesa",
    "Qatar": "Catariana",
    "Romania": "Romena",
    "Russia": "Russa",
    "Rwanda": "Ruandesa",
    "Saint Kitts and Nevis": "São-cristovense e Nevisiana",
    "Saint Lucia": "Santa-lucense",
    "Saint Vincent and the Grenadines": "São-vicentina e Granadina",
    "Samoa": "Samoana",
    "San Marino": "São-marinhense",
    "Sao Tome and Principe": "Santomense",
    "Saudi Arabia": "Saudita",
    "Senegal": "Senegalesa",
    "Serbia": "Sérvia",
    "Seychelles": "Seychellense",
    "Sierra Leone": "Serra-leonense",
    "Singapore": "Singapurense",
    "Slovakia": "Eslovaca",
    "Slovenia": "Eslovena",
    "Solomon Islands": "Ilhas Salomão",
    "Somalia": "Somali",
    "South Africa": "Sul-africana",
    "South Korea": "Sul-coreana",
    "South Sudan": "Sul-sudanesa",
    "Spain": "Espanhola",
    "Sri Lanka": "Sri-lankesa",
    "Sudan": "Sudanesa",
    "Suriname": "Surinamesa",
    "Sweden": "Sueca",
    "Switzerland": "Suíça",
    "Syria": "Síria",
    "Taiwan": "Taiwanesa",
    "Tajikistan": "Tajique",
    "Tanzania": "Tanzaniana",
    "Thailand": "Tailandesa",
    "Togo": "Togolesa",
    "Tonga": "Tonganesa",
    "Trinidad and Tobago": "Trinitária e Tobagense",
    "Tunisia": "Tunisiana",
    "Turkey": "Turca",
    "Turkmenistan": "Turcomena",
    "Tuvalu": "Tuvaluana",
    "Uganda": "Ugandesa",
    "Ukraine": "Ucraniana",
    "United Arab Emirates": "Emiradense",
    "United Kingdom": "Britânica",
    "United States": "Americana",
    "Uruguay": "Uruguaia",
    "Uzbekistan": "Uzbeque",
    "Vanuatu": "Vanuatuana",
    "Vatican City": "Vaticana",
    "Venezuela": "Venezuelana",
    "Vietnam": "Vietnamita",
    "Yemen": "Iemenita",
    "Zambia": "Zambiana",
    "Zimbabwe": "Zimbabuana",
    "Swedish": "Suíça",
}

import re

def traduzir_json(caminho_entrada, caminho_saida):
    # Carregar o arquivo JSON de entrada
    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)

    # Aplica traduções aos dados de cada atriz (cada elemento da lista)
    dados_traduzidos = [traduzir_dicionario(dicionario) for dicionario in dados_json]

    # Salva os dados traduzidos em um novo arquivo JSON
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        json.dump(dados_traduzidos, f, indent=2, ensure_ascii=False)

def traduzir_dicionario(dicionario):
    novo_dicionario = {}
    for chave, valor in dicionario.items():
        if chave == "mes_nascimento" and valor in traducoes_mes_nascimento:
            novo_dicionario[chave] = traducoes_mes_nascimento[valor]

        elif chave == "mes_morte" and valor in traducoes_mes_morte:
            novo_dicionario[chave] = traducoes_mes_morte[valor]

        elif chave == "etnia" and valor in traducoes_etnia:
            novo_dicionario[chave] = traducoes_etnia[valor]

        elif chave == "cor_cabelo" and valor in traducoes_cor_cabelo:
            novo_dicionario[chave] = traducoes_cor_cabelo[valor]

        elif chave == "cor_olhos" and valor in traducoes_cor_olhos:
            novo_dicionario[chave] = traducoes_cor_olhos[valor]

        elif chave == "piercings" and valor in traducoes_piercings:
            novo_dicionario[chave] = traducoes_piercings[valor]

        elif chave == "tattoos" and valor in traducoes_tattoos:
            novo_dicionario[chave] = traducoes_tattoos[valor]

        elif chave == "pais_nascimento" and valor in traducoes_pais_nascimento:
            novo_dicionario[chave] = traducoes_pais_nascimento[valor]

        elif chave == "status" and valor in traducoes_status:
            novo_dicionario[chave] = traducoes_status[valor]

        elif chave == "sexualidade" and valor in traducoes_sexualidade:
            novo_dicionario[chave] = traducoes_sexualidade[valor]

        elif chave == "seios" and valor in traducoes_seios:
            novo_dicionario[chave] = traducoes_seios[valor]

        elif chave == "nacionalidade" and valor in traducoes_nacionalidade:
            novo_dicionario[chave] = traducoes_nacionalidade[valor]

        elif chave == "quadril" and valor in traducoes_quadril:
            novo_dicionario[chave] = traducoes_quadril[valor]

        elif chave == "signo":
            # Verifica se o valor do signo contém informações adicionais entre parênteses
            match = re.match(r"^(.*?)\s+\((.*?)\)$", valor)
            if match:
                signo_traduzido = traducoes_signos.get(match.group(1), match.group(1))
                novo_dicionario[chave] = f"{signo_traduzido} ({match.group(2)})"
            else:
                novo_dicionario[chave] = traducoes_signos.get(valor, valor)
        elif chave == "profissao":
            # Dividir as profissões em uma lista e traduzir cada uma
            profissoes_traduzidas = [traduzir_profissao(p) for p in valor.split(',')]
            novo_dicionario[chave] = ", ".join(profissoes_traduzidas)
        elif isinstance(valor, dict):
            # Se o valor for um dicionário, aplicar recursivamente a tradução
            novo_dicionario[chave] = traduzir_dicionario(valor)
        else:
            # Manter outros tipos de valores sem tradução
            novo_dicionario[chave] = valor
    return novo_dicionario

def traduzir_profissao(profissao):
    # Traduz uma profissão específica usando um dicionário de tradução específico
    profissoes_traduzidas = []
    for p in profissao.split(','):
        p = p.strip()
        if p in traducoes_profissoes:
            profissoes_traduzidas.append(traducoes_profissoes[p])
        else:
            profissoes_traduzidas.append(p)  # Manter a mesma se não houver tradução
    return ", ".join(profissoes_traduzidas)

# Exemplo de uso:
if __name__ == "__main__":
    caminho_entrada = 'resultados/atrizes.json'
    caminho_saida = 'resultados/atrizes_traduzido-br.json'
    traduzir_json(caminho_entrada, caminho_saida)

    print("Dados das atrizes foram traduzidos e salvos em 'resultados/atrizes_traduzido-br.json'.")
