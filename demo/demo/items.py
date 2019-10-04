# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    publish_date = scrapy.Field()
    headline = scrapy.Field()
    author = scrapy.Field()
    review = scrapy.Field()
    rating = scrapy.Field()
    route = scrapy.Field()
    

