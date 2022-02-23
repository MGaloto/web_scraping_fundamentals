import requests
from bs4 import BeautifulSoup as BS

class Funciones:

    def Inicio(url):
        req = requests.get(url)
        respuesta = req.status_code
        if respuesta == 200:
            print('La respuesta es:',respuesta, ' de la URL: ',req.url)
        else:
            print('VER: La respuesta es:',respuesta, ' de la URL: ',req.url)
        return req



    def ScrapHeader(req):
        soup = BS(req.text, 'lxml')
        soup = soup.find('ul', attrs={'class': 'horizontal-list main-sections hide-on-dropdown'}).find_all('li')
        secciones = [seccion.a.get('href') for seccion in soup]
        return secciones

    def ScrapContent(urls):
        try:
            nota = requests.get(urls)
            if nota.status_code == 200:
                note = BS(nota.text, 'lxml')
                titulos = note.find('div', attrs= {'class': 'col 2-col'})
                titulouno = titulos.h1.get_text()
                titulodos = titulos.h4.get_text()
                texto  = titulos.h3
                print(titulouno,'\n' ,titulodos,'\n', texto)
        except Exception as e:
                print('Error: ',e)




        
