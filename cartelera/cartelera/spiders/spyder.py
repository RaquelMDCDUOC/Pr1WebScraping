# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from cartelera.items import CarteleraItem

class EcarteleraSpider(CrawlSpider):
    name = 'cartelera'
    item_count = 0
    allowed_domain = ['https://www.ecartelera.com']
    start_urls = ['https://www.ecartelera.com/listas/mejores-peliculas/']
    
    rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[@class="pagination"]/a[last()]'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@id="listaglobal"]//a')),
							callback = 'parse_item', follow = True)
	}
    
    def parse_item(self, response):
        ecartelera_item = CarteleraItem()
		#info de pelicula
        print("item: %s " % response)
        ecartelera_item['titulo'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[2]/text())').extract()
        ecartelera_item['tituloOriginal'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[2]/text())').extract()
        ecartelera_item['anyo'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[1]/span/text())').extract()
        ecartelera_item['pais'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[3]/text())').extract()
        ecartelera_item['duraccion'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[4]/span)').extract()
        ecartelera_item['presupuesto'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[5]/text())').extract()
        ecartelera_item['genero'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[6]/span)').extract()
       # ecartelera_item['estudio'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[1]/div/p[7]/span)').extract()
        ecartelera_item['ranking'] = response.xpath('normalize-space(//*[@id="bloc1"]/div[3]/div/div/p[2]/strong[1])').extract()

        yield ecartelera_item