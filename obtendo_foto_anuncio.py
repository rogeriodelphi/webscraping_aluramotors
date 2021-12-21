from IPython.core.display import display, HTML
from capturar_dados_anuncio import anuncio

image = anuncio.find('div', 'image-card').img
image.get('src')

# Visualizando a FOTO no notebook (extra)
display(HTML(str(anuncio.find('div', {'class': 'image-card'}).img)))
display(HTML("<img src=" + anuncio.find('div', {'class': 'image-card'}).img.get('src') + ">"))
print(image.get('src').split('/')[-1]) #pegando o endereço da imagem

from urllib.request import urlretrieve
urlretrieve(image.get('src'), 'C:\Projetos\Web Scraping\output\img/' + image.get('src').split('/')[-1])
