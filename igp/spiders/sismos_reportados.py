from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.contrib.loader import XPathItemLoader

from igp.items import SismoItem


class SismosReportadosSpider(BaseSpider):
    name = 'sismos_reportados'
    allowed_domains = ['igp.gob.pe']
    start_urls = ['http://www.igp.gob.pe/sismologia/sismo/IGPSIS/sismos_reportados.htm']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sismos = hxs.select('//area/@onmouseover').re("popup\((.*?)\)")
          
        for sismo in sismos:
            item = SismoItem()
            sismo = sismo.replace("'", "")
            sismo = sismo.split(',')

            item['fecha'] = sismo[0]
            item['hora'] = sismo[1]
            item['latitud'] = sismo[2]
            item['longitud'] = sismo[3]
            item['profundidad'] =  sismo[4]
            item['magnitud'] =  sismo[5]

            yield item
