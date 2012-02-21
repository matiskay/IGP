from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.contrib.loader import XPathItemLoader
from scrapylib.processors import default_input_processor, default_output_processor

from igp.items import Sismo 

class SismosReportadosLoader(XPathItemLoader):
    default_item_class = KrogerItem
    default_input_processor = default_input_processor
    default_output_processor = default_output_processor


class SismosReportadosSpider(BaseSpider):
    name = 'sismos_reportados'
    allowed_domains = ['igp.gob.pe']
    start_urls = ['http://www.igp.gob.pe/sismologia/sismo/IGPSIS/sismos_reportados.htm']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sismos = hxs.select('//area/@onmouseover').re("popup\((.*?)\)")
        
        for sismo in sismos:
