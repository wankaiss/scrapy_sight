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
    city = scrapy.Field()  # city
    scenic = scrapy.Field()  # 景点
    scenic_highlight = scrapy.Field()  # 景点亮点
    scenic_description = scrapy.Field()  # 景点描述
    scenic_address = scrapy.Field()  # 景点地址
    scenic_mobile = scrapy.Field()  # 景点电话
    scenic_open_time = scrapy.Field()  # 景点开放时间
    scenic_advice_time = scrapy.Field()  # 建议游玩时间
    scenic_ticket = scrapy.Field()  # 景点门票
    food = scrapy.Field()  # 美食地点
    food_description = scrapy.Field()  # 美食描述
    food_people_average = scrapy.Field()  # 人均
    food_special_food = scrapy.Field()  # 特色食物
    food_mobile = scrapy.Field()
    food_address = scrapy.Field()
    food_open_time = scrapy.Field()
    shopping = scrapy.Field()  # 购物地点
    shopping_description = scrapy.Field()  # 描述
    shopping_transport = scrapy.Field()
    shopping_mobile = scrapy.Field()
    shopping_address = scrapy.Field()
    shopping_open_time = scrapy.Field()


class ProxyIp(scrapy.Item):
    ip_port = scrapy.Field()
    user_pass = scrapy.Field()
