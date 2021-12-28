#WEB SCRAPING DO SITE ALURA MOTORS - OBTENDO OS DADOS DE TODOS OS ANÚNCIOS DE UMA PÁGINA

#Identificando as informações no HTML

from webscraping_aluramotors.criando_objeto_beautifulsoup import soup
#Importando as bibliotecas
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

# Mostrando a quantidade de cards por página
len(soup.find('div', {'id':'container-cards'}).findAll('div', class_='card'))

anuncios = soup.find('div', {'id':'container-cards'}).findAll('div', class_='card')


# Buscando todos os cards
for item in anuncios:
  # com o str converte de Beatifulsoup para string e com isso posso fazer a concatenação
  # salta duas linhas a cada card
  # print(str(item) + '\n\n')

# Declarando variável "cards"
  cards = []

# Obtendo a HTML
response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

#Obtendo as Tags de interesse - Uma lista com os cards
anuncios = soup.find('div', {'id':'container-cards'}).findAll('div', class_='card')


#Coletando informações dos Cards
for anuncio in anuncios:
    card = {}

    # Valor ------------------------------------------------------------
    card['value'] = anuncio.find('p', {'class': 'txt-value'}).get_text()

    # Informações ------------------------------------------------------
    # coletando todas as tag's <P> da div *body-card*
    info = anuncio.find('div', {'class': 'body-card'}).findAll('p')

    # para cada item na lista *info* adiciona-se no dicionário *card* a key
    # (nome da class) e o value (conteudo da class)

    for item in info:
        card[item.get('class')[0].split('-')[-1]] = item.get_text()

    # Acessórios -------------------------------------------------------
    itens = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
    itens.pop()

    acessorios = []
    for item in itens:
        acessorios.append(item.get_text().replace('► ', ''))
    card['items'] = acessorios

    # Adicionando resultados à lista "cards" ---------------------------

    cards.append(card)

    # Imagens ----------------------------------------------------------
    image = anuncio.find('div', 'image-card').img
    urlretrieve(image.get('src'), 'C:\Projetos\Web Scraping\output\img/' + image.get('src').split('/')[-1])

# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
dataset.to_csv('C:\Projetos\Web Scraping\output\data\dataset.csv', sep=';', index=False, encoding='utf-8-sig')
print(dataset)