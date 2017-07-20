# -*- coding: utf-8 -*-
import scrapy
from ..items import SightItem
from scrapy import log
import re


class SoloSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['baidu.com']
    start_urls = [
        "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%8E%AF%E7%90%83%E8%B4%B8%E6%98%93%E5%B9%BF%E5%9C%BA&ic=0&width=0&height=0"]  # 大厦描述

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
        print 'response_body: %s' % response.xpath('//div[@id="imgid"]/ul[@class="imglist"]').extract()
        # url = ''
        # for option in response.xpath('//div[@id="imgid"]'):
        #     # for option in response.xpath('//div[@id="imgid"]/ul/li')[0:5]:
        #     img_src = option.xpath('a/img/@src').extract_first()
        #     i = 0
        #     log.msg('img_src in line 54***********' + option.xpath('a/img/@src').extract_first(), log.INFO)
        #     if i == 4:
        #         url += img_src
        #     else:
        #         url += img_src + ','
        #         i += 1
        # print type(url), ':', url
