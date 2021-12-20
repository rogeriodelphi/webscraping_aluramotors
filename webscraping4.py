#Acessando as TAGS e seus atributos

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

#Melhorar a saída do HTML
print(soup.prettify())

#Acessando as TAGS
print(soup.title)
print(soup.div.div.div.div.h5)
print(soup.title.get_text())
print(soup.h5.get_text())
print(soup.get_text())

#Acessando os atributos de uma TAG
print(soup.img)
print(soup.img.attrs)
print(soup.img.attrs.keys())
print(soup.img.attrs.values())
print(soup.img['class'])
print(soup.img.get('class'))
print(soup.img.get('src'))