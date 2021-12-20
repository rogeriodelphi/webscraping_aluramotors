#Pesquisando com o BEAUTIFULSOUP

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/index.php'

response = urlopen(url)
html = response.read()

#Convertendo o Tipo bytes para string
html = html.decode('utf-8')

#Eliminando os caracteres de Tabulação, quebra de linha etc.
html.split()
" ".join(html.split())

#Eliminando os espaçoes em branco entre as TAGS
# " ".join(html.split()).replace('> <', '><')

#Função de tratamento de Strings
def trata_html(html):
    return " ".join(html.split()).replace('> <', '><')

html = trata_html(html)

soup = BeautifulSoup(html, 'html.parser')

#Método find()
print(soup.find('img'))

#Comando equivalente ao método find()
print(soup.findAll('img', limit = 2))

#Passando listas de TAGS
print(soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))


#Comando equivalente ao método find()
print(soup.findAll('img', limit = 2)[0])

#Atalho para o método *findAll()
print(soup('img'))

#Utilizando o argumento attributes
print(soup.findAll('p'))

#Buscando por conteúdo de uma TAG - Por nome ou por valor
print(soup.findAll('p', {'class':'txt-name'}))
print(soup.findAll('p', {'class':'txt-value'}))

#Pesquisando o conteúdo de uma TAG - Por nome
print(soup.findAll('p', text = "São Paulo - SP"))

#Utilizando diretamente os atributos
print(soup.findAll('img', alt = "Foto"))

#Lista de link das fotos
for item in soup.findAll('img', alt = "Foto"):
  print(item.get('src'))

#Cuidado com o atributo "class"
print(soup.findAll('p', class_='txt-value'))

#Obtendo todo o conteúdo de texto de uma página
print(soup.findAll(text = True))