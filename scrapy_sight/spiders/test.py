# -*- coding: utf-8 -*-

import scrapy
import re


class RestaurantSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['ctrip.com']
    start_urls = ['http://you.ctrip.com/food/hangzhou14/5140504.html']

    def start_requests(self):
        """
        :description
           根据geoapi查询位置坐标       
        :return: 
        """
        for url in self.start_urls:
            yield scrapy.Request(url, self.baike_parse)

    def baike_parse(self, response):
        import chardet
        print chardet.detect(response.body)

if __name__ == '__main__':
    list_test = []
    list_test.append('a')
    list_test.append('b')
    list_test.append('c')
    print list_test
