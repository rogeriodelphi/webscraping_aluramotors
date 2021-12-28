#  WEB SCRAPING DO SITE ALURA MOTORS - OBTENDO OS DADOS DE TODOS OS ANÚNCIOS DO SITE

# Identificando as informações no HTML
# Busca o número de itens por página e converte para inteiro

from webscraping_aluramotors.criando_objeto_beautifulsoup import soup

print(int(soup.find('span', {'class':'info-pages'}).get_text().split()[-1]))

# Criando uma rotina de scraping
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

# criando a lista *cards*
cards = []

# obtendo a HTML e a quantidade de páginas atuais
response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
pages = int(soup.find('span', {'class': 'info-pages'}).get_text().split()[-1])

# iteração de páginas

for item in range(pages):

    # obtendo a HTML
    response = urlopen('https://alura-site-scraping.herokuapp.com/index.php?page=' + str(item + 1))
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # tag de interesse
    anuncios = soup.find('div', {'id': 'container-cards'}).findAll('div', class_='card')

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
        from urllib.request import urlretrieve

        urlretrieve(image.get('src'), 'C:\Projetos\Web Scraping\output\img/' + image.get('src').split('/')[-1])

        print(cards)