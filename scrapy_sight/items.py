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
    id_num = scrapy.Field()


class CtripSightItem(scrapy.Item):
    continent = scrapy.Field()  # 洲
    area = scrapy.Field()  # 区域
    country = scrapy.Field()  # 国家
    city = scrapy.Field()  # city.py
    scenic = scrapy.Field()  # 景点
    scenic_url = scrapy.Field()
    scenic_ticket = scrapy.Field()  # 景点门票
    food = scrapy.Field()  # 美食地点
    food_url = scrapy.Field()
    shopping = scrapy.Field()  # 购物地点
    shopping_url = scrapy.Field()


class ProxyIp(scrapy.Item):
    ip_port = scrapy.Field()
    user_pass = scrapy.Field()


class PoiItem(scrapy.Item):
    city = scrapy.Field()
    destination = scrapy.Field()
    name = scrapy.Field()
    mobile = scrapy.Field()
    open_hours = scrapy.Field()
    description = scrapy.Field()
    photo_reference = scrapy.Field()
    comment = scrapy.Field()
    recommend = scrapy.Field()
    recommend_food = scrapy.Field()
    people_average = scrapy.Field()
    subtitle = scrapy.Field()
    address = scrapy.Field()
    hotel_star = scrapy.Field()
    food_series = scrapy.Field()
    lat = scrapy.Field()
    ticket = scrapy.Field()
    advice_time = scrapy.Field()
    lng = scrapy.Field()
    google_message = scrapy.Field()
