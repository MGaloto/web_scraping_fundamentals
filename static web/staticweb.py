import requests
from lxml import html


url = 'https://www.wikipedia.org/'


# Para hacer el requerimiento usamos la libreria requests
# Lo que me devuelve la funcion la guardamos en la variable respuesta

respuesta = requests.get(url)

# El siguiente comando transforma en un parseador la respuesta y nos permite muchas tecnicas para acceder a los elementos.

parser = html.fromstring(respuesta.text)

# Guardamos en una variable un elemento que contiene el siguiente id:

ingles = parser.get_element_by_id('js-link-box-en')

# El parseador nos devuelve una clase, para poder ver el contenido hay que agregarle text_content()

print(ingles.text_content())


# Puedo obtener esto mismo utilizando XPATH

ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

print(ingles)


# Para obtener todos los idiomas: Los textos estan dentro de <a> y dentro de un <div>, cada <a> tiene distinto Id, el patron en realidad se encuentra en el tag <div>, todos tienen la clase central-featured-lang. La clase tiene que contenerlo.

# Esta expresion hace match con varios elementos y los almacena en una lista.

idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print(idioma)

# Se puede hacer exactamente lo mismo utilizando otra funcion de parser

idiomas = parser.find_class('central-featured-lang')

for idioma in idiomas:
    print(idioma.text_content())
    
    
# IMPORTANTE: Si dentro de una class hay un espacio es porque son dos class diferentes. Ejemplo: class="central-featured-lang lang2"
    


#%%

# Utilizaremos beautifoulsop en vez de lxml.

# Scrap de StackOverflow, titulo y descripcion.

from bs4 import BeautifulSoup as BS
# bs es otro parseador que funciona parecido a lxml

import requests

url = 'https://stackoverflow.com/questions'

respuesta = requests.get(url)

# Ya no se llama parser sino que se llama soup, aqui buscaremos las etiquetas

soup = BS(respuesta.text)

contenedor_de_preguntas = soup.find(id="questions")

# A partir de este elemento obtengo todos los hijos:
    

lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="s-post-summary")


for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find(class_="s-post-summary--content-excerpt").text
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip() #Strip elimina los espacios
    print(texto_pregunta)
    print(descripcion_pregunta)
    
    print()


# ¿Cual es la ventaja de BS?, una de las ventajas es que podemos utilizar find_next_sibiling('etiqueta') que nos permite capturar la siguiente etiqueta que estamos consultando, no solo por clase y por id sino que tambien podemos buscar el proximo elemento con este comando.






#%%

