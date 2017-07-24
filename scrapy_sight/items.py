# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SightItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    lng = scrapy.Field()
    lat = scrapy.Field()
    pinyin = scrapy.Field()


class ProxyIp(scrapy.Item):
    ip_port = scrapy.Field()
    user_pass = scrapy.Field()
