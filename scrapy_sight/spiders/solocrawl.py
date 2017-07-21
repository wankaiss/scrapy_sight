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
        host_address = 'http://image.baidu.com'
        path = response.xpath('//*[@id="page"]/a[10]/@href').extract_first()
        url = host_address.encode('utf-8') + path
        print url
        for option in response.xpath('//div[@id="imgid"]/ul[@class="imglist"]/li[@class="imgitem"]')[19:]:
            item_final = SightItem()
            item_final['title'] = 'title'
            item_final['lng'] = 'lng'
            item_final['lat'] = 'lat'
            item_final['description'] = 'description'
            item_final['category'] = 'category'
            img_src = option.xpath('a/@href').extract_first()
            result = re.search(r'.*objurl=(http.*?)&.*', img_src).groups()[0]
            img_src = urllib.unquote(urllib.unquote(result)).encode('utf-8')
            item_final['url'] = img_src
            if img_src is None or len(img_src) == 0:
                item_final['url'] = 'url_null'
                log.msg('img_src is null==============' + img_src, level=log.INFO)
            log.msg('img_src in line 61***********' + img_src + '; type: %s ' % type(img_src), log.INFO)
            log.msg('img_src: ' + img_src + ' at line 76', level=log.INFO)
            log.msg('run out picture_parse at line 77', level=log.INFO)
            yield item_final

        for i in range(0, 2):
            if path:
                yield scrapy.Request(url, meta={'splash': {
                                                    'endpoint': 'render.html',
                                                    'args': {'wait': 0.5}
                                                }
                                                }, callback=self.parse)

