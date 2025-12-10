import json

# Dicionários de tradução para cada campo específico

import json
import re

import json
import re

traducciones_tamano_sujetador = {
    "Unknown": "",
}

traducciones_cadera = {
    "Unknown": "",
    "Fake": "Silicona",
    "Natural": "Natural",
}

traducciones_senos = {
    "Unknown": "",
    "Fake": "Silicona",
    "Natural": "Natural",
}

traducciones_sexualidad = {
    "Unknown": "",
    "Bi-Sexual": "Bisexual",
    "Straight": "Heterosexual",
    "Lesbian": "Lesbiana",
    "Gay": "Gay",
    "Pansexual": "Pansexual",
}

traducciones_estado = {
    "Unknown": "",
    "Active": "Activa",
    "Retired": "Jubilada",
    "Deceased": "Fallecida",
}

traducciones_profesiones = {
    "Unknown": "",
    "Adult Model": "Modelo Adulta",
    "Porn Star": "Actriz Porno",
    "Centerfold": "Centrofold",
    "Actress": "Actriz",
    "Musician": "Música",
    "Celebrities": "Celebridades",
}

traducciones_signos = {
    "Unknown": "",
    "Aries": "Aries",
    "Taurus": "Tauro",
    "Gemini": "Géminis",
    "Cancer": "Cáncer",
    "Leo": "Leo",
    "Virgo": "Virgo",
    "Libra": "Libra",
    "Scorpio": "Escorpio",
    "Sagittarius": "Sagitario",
    "Capricorn": "Capricornio",
    "Aquarius": "Acuario",
    "Pisces": "Piscis",
}

traducciones_mes_nacimiento = {
    "Unknown": "",
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre",
}

traducciones_mes_muerte = {
    "Unknown": "",
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre",
}

traducciones_etnia = {
    "Unknown": "",
    "Asian": "Asiática",
    "Caucasian": "Caucásica",
    "Latin": "Latina",
    "Black": "Negra",
    "Mixed": "Mixta",
}

traducciones_color_cabello = {
    "Unknown": "",
    "Black": "Negro",
    "Brown": "Castaño",
    "Blonde": "Rubio",
    "Red": "Pelirrojo",
}

traducciones_color_ojos = {
    "Unknown": "",
    "Brown": "Marrones",
    "Blue": "Azules",
    "Green": "Verdes",
    "Hazel": "Avellana",
}

traducciones_piercings = {
    "Unknown": "",
    "Yes": "Sí",
    "No": "No",
}

traducciones_tatuajes = {
    "Unknown": "",
    "Yes": "Sí",
    "No": "No",
}

traducciones_pais_nacimiento = {
    "Unknown": "",
    "Afghanistan": "Afganistán",
    "Albania": "Albania",
    "Algeria": "Argelia",
    "Andorra": "Andorra",
    "Angola": "Angola",
    "Antigua and Barbuda": "Antigua y Barbuda",
    "Argentina": "Argentina",
    "Armenia": "Armenia",
    "Australia": "Australia",
    "Austria": "Austria",
    "Azerbaijan": "Azerbaiyán",
    "Bahamas": "Bahamas",
    "Bahrain": "Baréin",
    "Bangladesh": "Bangladesh",
    "Barbados": "Barbados",
    "Belarus": "Bielorrusia",
    "Belgium": "Bélgica",
    "Belize": "Belice",
    "Benin": "Benín",
    "Bhutan": "Bután",
    "Bolivia": "Bolivia",
    "Bosnia and Herzegovina": "Bosnia y Herzegovina",
    "Botswana": "Botsuana",
    "Brazil": "Brasil",
    "Brunei": "Brunéi",
    "Bulgaria": "Bulgaria",
    "Burkina Faso": "Burkina Faso",
    "Burundi": "Burundi",
    "Cabo Verde": "Cabo Verde",
    "Cambodia": "Camboya",
    "Cameroon": "Camerún",
    "Canada": "Canadá",
    "Central African Republic": "República Centroafricana",
    "Chad": "Chad",
    "Chile": "Chile",
    "China": "China",
    "Colombia": "Colombia",
    "Comoros": "Comoras",
    "Congo, Democratic Republic of the": "República Democrática del Congo",
    "Congo, Republic of the": "República del Congo",
    "Costa Rica": "Costa Rica",
    "Croatia": "Croacia",
    "Cuba": "Cuba",
    "Cyprus": "Chipre",
    "Czechia": "Chequia",
    "Denmark": "Dinamarca",
    "Djibouti": "Yibuti",
    "Dominica": "Dominica",
    "Dominican Republic": "República Dominicana",
    "East Timor": "Timor Oriental",
    "Ecuador": "Ecuador",
    "Egypt": "Egipto",
    "El Salvador": "El Salvador",
    "Equatorial Guinea": "Guinea Ecuatorial",
    "Eritrea": "Eritrea",
    "Estonia": "Estonia",
    "Eswatini": "Esuatini",
    "Ethiopia": "Etiopía",
    "Fiji": "Fiyi",
    "Finland": "Finlandia",
    "France": "Francia",
    "Gabon": "Gabón",
    "Gambia": "Gambia",
    "Georgia": "Georgia",
    "Germany": "Alemania",
    "Ghana": "Ghana",
    "Greece": "Grecia",
    "Grenada": "Granada",
    "Guatemala": "Guatemala",
    "Guinea": "Guinea",
    "Guinea-Bissau": "Guinea-Bisáu",
    "Guyana": "Guyana",
    "Haiti": "Haití",
    "Honduras": "Honduras",
    "Hungary": "Hungría",
    "Iceland": "Islandia",
    "India": "India",
    "Indonesia": "Indonesia",
    "Iran": "Irán",
    "Iraq": "Irak",
    "Ireland": "Irlanda",
    "Israel": "Israel",
    "Italy": "Italia",
    "Jamaica": "Jamaica",
    "Japan": "Japón",
    "Jordan": "Jordania",
    "Kazakhstan": "Kazajistán",
    "Kenya": "Kenia",
    "Kiribati": "Kiribati",
    "Korea, North": "Corea del Norte",
    "Korea, South": "Corea del Sur",
    "Kosovo": "Kosovo",
    "Kuwait": "Kuwait",
    "Kyrgyzstan": "Kirguistán",
    "Laos": "Laos",
    "Latvia": "Letonia",
    "Lebanon": "Líbano",
    "Lesotho": "Lesoto",
    "Liberia": "Liberia",
    "Libya": "Libia",
    "Liechtenstein": "Liechtenstein",
    "Lithuania": "Lituania",
    "Luxembourg": "Luxemburgo",
    "Madagascar": "Madagascar",
    "Malawi": "Malaui",
    "Malaysia": "Malasia",
    "Maldives": "Maldivas",
    "Mali": "Malí",
    "Malta": "Malta",
    "Marshall Islands": "Islas Marshall",
    "Mauritania": "Mauritania",
    "Mauritius": "Mauricio",
    "Mexico": "México",
    "Micronesia": "Micronesia",
    "Moldova": "Moldavia",
    "Monaco": "Mónaco",
    "Mongolia": "Mongolia",
    "Montenegro": "Montenegro",
    "Morocco": "Marruecos",
    "Mozambique": "Mozambique",
    "Myanmar": "Myanmar",
    "Namibia": "Namibia",
    "Nauru": "Nauru",
    "Nepal": "Nepal",
    "Netherlands": "Países Bajos",
    "New Zealand": "Nueva Zelanda",
    "Nicaragua": "Nicaragua",
    "Niger": "Níger",
    "Nigeria": "Nigeria",
    "North Macedonia": "Macedonia del Norte",
    "Norway": "Noruega",
    "Oman": "Omán",
    "Pakistan": "Pakistán",
    "Palau": "Palaos",
    "Palestine": "Palestina",
    "Panama": "Panamá",
    "Papua New Guinea": "Papúa Nueva Guinea",
    "Paraguay": "Paraguay",
    "Peru": "Perú",
    "Philippines": "Filipinas",
    "Poland": "Polonia",
    "Portugal": "Portugal",
    "Qatar": "Catar",
    "Romania": "Rumania",
    "Russia": "Rusia",
    "Rwanda": "Ruanda",
    "Saint Kitts and Nevis": "San Cristóbal y Nieves",
    "Saint Lucia": "Santa Lucía",
    "Saint Vincent and the Grenadines": "San Vicente y las Granadinas",
    "Samoa": "Samoa",
    "San Marino": "San Marino",
    "Sao Tome and Principe": "Santo Tomé y Príncipe",
    "Saudi Arabia": "Arabia Saudita",
    "Senegal": "Senegal",
    "Serbia": "Serbia",
    "Seychelles": "Seychelles",
    "Sierra Leone": "Sierra Leona",
    "Singapore": "Singapur",
    "Slovakia": "Eslovaquia",
    "Slovenia": "Eslovenia",
    "Solomon Islands": "Islas Salomón",
    "Somalia": "Somalia",
    "South Africa": "Sudáfrica",
    "South Sudan": "Sudán del Sur",
    "Spain": "España",
    "Sri Lanka": "Sri Lanka",
    "Sudan": "Sudán",
    "Suriname": "Surinam",
    "Sweden": "Suecia",
    "Switzerland": "Suiza",
    "Syria": "Siria",
    "Taiwan": "Taiwán",
    "Tajikistan": "Tayikistán",
    "Tanzania": "Tanzania",
    "Thailand": "Tailandia",
    "Togo": "Togo",
    "Tonga": "Tonga",
    "Trinidad and Tobago": "Trinidad y Tobago",
    "Tunisia": "Túnez",
    "Turkey": "Turquía",
    "Turkmenistan": "Turkmenistán",
    "Tuvalu": "Tuvalu",
    "Uganda": "Uganda",
    "Ukraine": "Ucrania",
    "United Arab Emirates": "Emiratos Árabes Unidos",
    "United Kingdom": "Reino Unido",
    "United States": "Estados Unidos",
    "Uruguay": "Uruguay",
    "Uzbekistan": "Uzbekistán",
    "Vanuatu": "Vanuatu",
    "Vatican City": "Ciudad del Vaticano",
    "Venezuela": "Venezuela",
    "Vietnam": "Vietnam",
    "Yemen": "Yemen",
    "Zambia": "Zambia",
    "Zimbabwe": "Zimbabue"
  }

import json
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
        if chave == "mes_nascimento" and valor in traducciones_mes_nacimiento:
            novo_dicionario[chave] = traducciones_mes_nacimiento[valor]

        elif chave == "mes_morte" and valor in traducciones_mes_muerte:
            novo_dicionario[chave] = traducciones_mes_muerte[valor]

        elif chave == "etnia" and valor in traducciones_etnia:
            novo_dicionario[chave] = traducciones_etnia[valor]

        elif chave == "cor_cabelo" and valor in traducciones_color_cabello:
            novo_dicionario[chave] = traducciones_color_cabello[valor]

        elif chave == "cor_olhos" and valor in traducciones_color_ojos:
            novo_dicionario[chave] = traducciones_color_ojos[valor]

        elif chave == "piercings" and valor in traducciones_piercings:
            novo_dicionario[chave] = traducciones_piercings[valor]

        elif chave == "tattoos" and valor in traducciones_tatuajes:
            novo_dicionario[chave] = traducciones_tatuajes[valor]

        elif chave == "pais_nascimento" and valor in traducciones_pais_nacimiento:
            novo_dicionario[chave] = traducciones_pais_nacimiento[valor]

        elif chave == "status" and valor in traducciones_estado:
            novo_dicionario[chave] = traducciones_estado[valor]

        elif chave == "sexualidade" and valor in traducciones_sexualidad:
            novo_dicionario[chave] = traducciones_sexualidad[valor]

        elif chave == "seios" and valor in traducciones_tamano_sujetador:
            novo_dicionario[chave] = traducciones_tamano_sujetador[valor]

        elif chave == "nacionalidade" and valor in traducciones_pais_nacimiento:
            novo_dicionario[chave] = traducciones_pais_nacimiento[valor]

        elif chave == "quadril" and valor in traducciones_cadera:
            novo_dicionario[chave] = traducciones_cadera[valor]

        elif chave == "signo":
            # Verifica se o valor do signo contém informações adicionais entre parênteses
            match = re.match(r"^(.*?)\s+\((.*?)\)$", valor)
            if match:
                signo_traduzido = traducciones_signos.get(match.group(1), match.group(1))
                novo_dicionario[chave] = f"{signo_traduzido} ({match.group(2)})"
            else:
                novo_dicionario[chave] = traducciones_signos.get(valor, valor)

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
        if p in traducciones_profesiones:
            profissoes_traduzidas.append(traducciones_profesiones[p])
        else:
            profissoes_traduzidas.append(p)  # Manter a mesma se não houver tradução
    return ", ".join(profissoes_traduzidas)

# Exemplo de uso:
if __name__ == "__main__":
    caminho_entrada = 'resultados/atrizes.json'
    caminho_saida = 'resultados/atrizes_traduzido-es.json'
    traduzir_json(caminho_entrada, caminho_saida)

    print("Dados das atrizes foram traduzidos e salvos em 'resultados/atrizes_traduzido-es.json'.")
