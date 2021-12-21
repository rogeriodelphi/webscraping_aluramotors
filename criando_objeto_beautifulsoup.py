#Obtendo o HTML e criando o objeto BeautifulSoup
from urllib.request import urlopen

from bs4 import BeautifulSoup

response = urlopen('https://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
