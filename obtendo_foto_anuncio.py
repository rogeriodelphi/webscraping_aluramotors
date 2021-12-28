from IPython.core.display import display, HTML
from capturar_dados_anuncio import anuncio
from urllib.request import urlretrieve

image = anuncio.find('div', {'class':'image-card'}).img
# image


# Obter o valor de um atributo
image.get('src')

#Exibindo um link clicável
print(image.get('src'))

# Visualizando a FOTO no notebook (extra)
display(HTML(str(anuncio.find('div', {'class': 'image-card'}).img)))
display(HTML("<img src=" + anuncio.find('div', {'class': 'image-card'}).img.get('src') + ">"))
print(image.get('src').split('/')[-1]) #pegando o endereço da imagem

#Rotina para acessar e salvar a FOTO do anúncio
#Pegando o nome da imagem
print('Nome da imagem: ' + image.get('src').split('/')[-1]) #pegando o endereço da imagem

#A função urlretrieve(url, filename) é utilizada para copiar um objeto de rede, indicado por uma URL, para um arquivo local.
#A função urlretrieve(url, filename) precisa de dois argumentos para copiar os dados para um arquivo local.
urlretrieve(image.get('src'), 'C:\Projetos\Web Scraping\output\img/' + image.get('src').split('/')[-1])
