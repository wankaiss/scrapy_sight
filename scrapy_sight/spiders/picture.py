# -*- coding: utf-8 -*-

import scrapy


class PictureCrawl(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['baidu.com']
    start_urls = ['http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=金茂大厦&ic=0&width=0&height=0']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        for option in response.xpath('//div[@id="imgid"]/ul[@class="imglist"]/li[@class="imgitem"]')[0:5]:
            print option.xpath('a/img/@src').extract_first()

    # def parse(self, response):
    #     result = response.xpath('//div[@id="imgid"]/ul').extract()
    #     print result
