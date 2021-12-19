#Tratamento de strings

from urllib.request import urlopen

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

print(html)