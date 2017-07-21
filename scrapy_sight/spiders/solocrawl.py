# -*- coding: utf-8 -*-
import scrapy
from ..items import SightItem
from scrapy import log
import re
import urllib


class SoloSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['baidu.com']
    start_urls = [
        "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E4%B8%8A%E6%B5%B7%E4%B8%AD%E5%BF%83%E5%A4%A7%E5%8E%A6&pn=0&gsm=64&ct=&ic=0&lm=-1&width=0&height=0"]  # 大厦描述

    # start_urls = ["http://www.sohu.com/a/150475260_451024"]  # 大厦描述

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        host_address = 'http://image.baidu.com'
        path = response.xpath('//*[@id="page"]/a[10]/@href').extract_first()
        page_num = response.xpath('//div[@id="page"]/strong/span/text()').extract_first()
        url = host_address.encode('utf-8') + path
        print 'page_num: %s' % page_num
        print 'url: %s' % url
        if page_num <= u'3':
            print 'run into page_num < 3 condition'
            yield scrapy.Request(url, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            }, callback=self.parse)

