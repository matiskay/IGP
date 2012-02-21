# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Sismo(Item):
    # define the fields for your item here like:
    fecha = Field()
    hora = Field()
    latitud = Field()
    longitud = Field()
    profundidad = Field()
    magnitud = Field()
