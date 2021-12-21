#WEB SCRAPING DO SITE ALURA MOTORS - OBTENDO OS DADOS DE UM ANÚNCIO

# Identificando e selecionando os dados no HTML Obtendo o HTML e criando o objeto BeautifulSoup

from criando_objeto_beautifulsoup import soup

#Criando variávels para armazenar informações
cards = []
card = {}

#Obtendo os dados do primeiro CARD
anuncio = soup.find('div', {'class':'well card'})
# print(anuncio)

#Obtendo o VALOR do veículo anunciado
# anuncio.find('div', {'class':'col-md-3 value-card'})
# anuncio.find('p', {'class':'txt-value'})
anuncio.find('p', {'class':'txt-value'}).get_text()
# print(anuncio)

#Jogando a informação para dentro do card
card['value'] = anuncio.find('p', {'class':'txt-value'}).get_text()
# print(card)


#1.3. Obtendo as INFORMAÇÕES sobre o veículo anunciado
# info = anuncio.find('div', {'class':'body-card'}).findAll('p')
# print(info)

infos = anuncio.find('div', {'class':'body-card'}).findAll('p')
# for info in infos:
#   print(info.get('class'), ' - ', info.get_text())

#Removendo o txt
# for info in infos:
#   print(info.get('class')[0].split('-')[-1], ' - ', info.get_text())

#Atualizando as informações para dentro do card
# for info in infos:
#     card[info.get('class')[0].split('-')[-1]] = info.get_text()
# print(card)

#RESUMO
#Todos os passos anteriores poderiam ser resumido a esse abaixo:
# infos = anuncio.find('div', {'class':'body-card'}).findAll('p')
# for info in infos:
#     card[info.get('class')[0].split('-')[-1]] = info.get_text()
# print(card)

#1.4. Obtendo os ACESSÓRIOS do veículo anunciado
anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')
items = anuncio.find('div', {'class': 'body-card'}).ul.findAll('li')

#Removendo o último item da lista
items.pop()

#Removendo caracteres indesejados
for item in items:
  item.getText().replace('►', '')

#Criando uma lista chamada "acessorios" e adicionando os items para dentro dela
acessorios = []
for item in items:
  acessorios.append(item.getText().replace('►', ''))
# print(acessorios)

#Atualizando as informações para dentro do card
card['items'] = acessorios
# print(card)

#Resumo
#Todos os passos anteriores poderiam ser resumido a esse abaixo:
# Acessórios
itens = anuncio.find('div', {'class':'body-card'}).ul.findAll('li')
itens.pop()

acessorios = []
for item in itens:
    acessorios.append(item.get_text().replace('► ', ''))
card['items'] = acessorios
print(card)

#1.5 Criando um DataFrame com os dados coletados do Alura Motors
import pandas as pd

#Criando um Dataset
dataset = pd.DataFrame(card)
dataset = pd.DataFrame.from_dict(card, orient='index').T
print(dataset)

#Criando o arquivo .csv e exportando os dados
dataset.to_csv('C:\Projetos\Web Scraping\output\data\card-dataset.csv', sep=';', index = False, encoding='utf-8-sig')
