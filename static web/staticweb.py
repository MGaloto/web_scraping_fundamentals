
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

print(idiomas)




#%%