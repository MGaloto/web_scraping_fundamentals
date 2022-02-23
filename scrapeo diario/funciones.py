import requests
from bs4 import BeautifulSoup as BS
import json

class Funciones:

    def Inicio(url):
        req = requests.get(url)
        respuesta = req.status_code
        if respuesta == 200:
            print('La respuesta es:',respuesta, ' de la URL: ',req.url)
        else:
            print('VER: La respuesta es:',respuesta, ' de la URL: ',req.url)
        return req


    def ScrapLinks(req):
        soup = BS(req.text, 'lxml')
        soup = soup.find('ul', attrs={'class': 'horizontal-list main-sections hide-on-dropdown'}).find_all('li')
        secciones = [seccion.a.get('href') for seccion in soup]
        return secciones

    def ScrapContent(links):
        notapagina = []
        for urls in links:
            try:
                nota = requests.get(urls)
                if nota.status_code == 200:
                    note = BS(nota.text, 'lxml')
                    titulos = note.find('div', attrs= {'class': 'col 2-col'})
                    try:
                        titulo = titulos.h1.get_text()
                    except:
                        titulo = None
                    try:
                        encabezado = titulos.h4.get_text()
                    except:
                        encabezado = None
                    try:
                        texto  = titulos.find('h3').text
                    except:
                        texto = None

                    elementos = {
                        'Titulo': titulo,
                        'Encabezado' : encabezado,
                        'Texto': texto,
                        'url': urls
                    }

                    notapagina.append(elementos)

                    #print(' Titulo: ',titulo,'\n' ,'Encabezado: ',encabezado,'\n', 'Texto: ',texto)
                    #print('\n')
            except Exception as e:
                    print('Error: ',e)
        return notapagina


    def SaveJson(lista_final):
        with open('notas.json', 'w', encoding='utf-8') as archivo_json_notas:
            json.dump(lista_final, archivo_json_notas, ensure_ascii=False, indent = 2)





        
