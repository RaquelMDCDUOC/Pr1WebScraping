# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarteleraItem(scrapy.Item):
    titulo = scrapy.Field()
    tituloOriginal = scrapy.Field()
    anyo = scrapy.Field()
    pais = scrapy.Field()
    duraccion = scrapy.Field()
    presupuesto = scrapy.Field()
    genero = scrapy.Field()
    ranking = scrapy.Field()
    pass
