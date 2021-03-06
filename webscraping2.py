#Obtendo o conteúdo HTML de um site

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://www.alura.com.br'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

try:
  req = Request(url, headers = headers)
  response = urlopen(req)
  print(response.read())
except HTTPError as e:
  print(e.status, e.reason)

except URLError as e:
  print(e.reason)  