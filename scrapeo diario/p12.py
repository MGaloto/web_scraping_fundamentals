from funciones import Funciones
import requests
from bs4 import BeautifulSoup as BS


url = 'https://www.pagina12.com.ar'

# Respuesta de peticion:

Funciones.Inicio(url)

# Vista del encabezado:

lista_encabezado = Funciones.ScrapHeader(requests.get(url))

# Recorrido del encabezado:

links = []

for lista in lista_encabezado:
    req = requests.get(lista)
    #print('Status Code: ',req.status_code, 'Link: ',lista)
    soup = BS(req.text, 'lxml')
    articulos = soup.find_all('div', attrs={'class': 'article-item__content'})
    for art in articulos:
        try:
            link = url + art.a.get('href')
            #print(link, '\n')
            links.append(link)
        except Exception as e:
            print('Error en la request')
            print(e)
            print('\n')

print(f'La lista contiene {len(links)} links')


for link in links:
    print(Funciones.ScrapContent(link))

