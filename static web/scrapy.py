
# Usando scrapy

# En scrapy primero hay que definir la clase de abstraccion, nuestro item en este caso es cada una de las preguntas de stakoverflow, queremos sacar el titulo y descripcion. Tenemos definido el item y las propiedades

from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader



class Pregunta(Item):
    id = Field()
    pregunta = Field()
    descripcion = Field()



# Esta clase va a ser el parseo

class StackOverflowSpider(Spider):
    name = 'MiPrimerSpider'
    
    start_urls = ['https://stackoverflow.com/questions']
    # Solo con definir la url scrapy ya hace el parseo
    def parse(self, response):
        # Este selector me sirve para hacerle consultas a la pagina
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="s-post-summary"]')
        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_xpath('descripcion', './/div[@class="s-post-summary--content-excerpt"]/text()')
            item.add_value('id', 1)
            
            yield item.load_item()











#%%

