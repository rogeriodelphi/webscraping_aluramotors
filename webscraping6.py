#Pesquisando com o BEAUTIFULSOUP - Outros métodos de pesquisas

from bs4 import BeautifulSoup

#Outros métodos de pesquisas
html_teste = '''
    <html>
    <body>
        <div id="container-a">
            <h1>Título A</h1>
            <h2 class="ref-a">Sub título A</h2>
            <p>Texto de conteúdo A</p>
        </div>
        <div id="container-b">
            <h1>Título B</h1>
            <h2 class="ref-b">Sub título B</h2>
            <p>Texto de conteúdo B</p>
        </div>
    </body>
</html>
'''

#Função de tratamento de Strings
def trata_html(input):
    return " ".join(input.split()).replace('> <', '><')

#Tratamentos para a string HTML
html_teste = trata_html(html_teste)
print(html_teste)

#Criando o objeto BeautifulSoup
soup = BeautifulSoup(html_teste, 'html.parser')
print(soup)

#Parents
print(soup.find('h2'))

print(soup.find('h2').find_parents())

for item in soup.findAll('h2'):
    print(item.find_parent('div'))

# Siblings
print(soup.find('h2').findNextSibling())
print(soup.find('h2').findPreviousSibling())
print(soup.find('p').findPreviousSiblings())

#Next e Previous
print(soup.find('h2').findNext())
print(soup.find('h2').findPrevious())
print(soup.find('h2').findAllNext())