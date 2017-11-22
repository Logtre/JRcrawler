# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JRcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()

class AlllinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()

class AllhtmlItem(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
    timestamp = scrapy.Field()
