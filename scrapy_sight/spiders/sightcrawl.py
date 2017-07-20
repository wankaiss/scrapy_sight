# -*- coding: utf-8 -*-
import scrapy
from ..items import SightItem
import re
from ..geo_api import baidu_geo_api, landmark
from scrapy import log


class SightSpider(scrapy.Spider):
    name = 'sight'
    allowed_domains = ['baidu.com']
    start_urls = ["http://image.baidu.com"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        for build in landmark[0:5]:
            item = SightItem()
            log.msg('build: ' + build, level=log.INFO)
            lng, lat = baidu_geo_api(build.encode('utf-8'))
            item['lng'] = lng
            item['lat'] = lat
            item['category'] = u'中国地标建筑'
            item['title'] = build.encode('utf-8')
            if lng == 1 or lat == 1:
                log.msg('no landmark found: ' + 'at line 33,' + build, level=log.INFO)
                continue
            baike_url = 'https://baike.baidu.com/item/%s' % build
            yield scrapy.Request(baike_url, meta={'item': item}, callback=self.content_parse)

    def content_parse(self, response):
        log.msg('run into content_parse at line 40', level=log.INFO)
        item = response.meta['item']
        result = response.xpath(
            '//div[@class="main-content"]/div[@class="lemma-summary"]/div[@class="para"]').extract()  # 大厦描述
        pattern = re.compile(r'<[^>]+>', re.S)
        description = pattern.sub('', result[0]).encode('utf-8')
        if len(result) == 0:
            description = 'description_null'
            log.msg('description_null in line 45', level=log.INFO)
        item['description'] = description
        picture_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&ic=0&width=0&height=0' % item['title'].decode('utf-8')
        log.msg('picture_url: ' + picture_url, level=log.INFO)
        log.msg('run out content_parse at line 51', level=log.INFO)
        yield scrapy.Request(picture_url, meta={'item': item,
                                                'splash': {
                                                    'endpoint': 'render.html',
                                                    'args': {'wait': 0.5}
                                                }
                                                }, callback=self.picture_parse)

    def picture_parse(self, response):
        log.msg('run into picture_parse at line 56', level=log.INFO)
        item = response.meta['item']
        for option in response.xpath('//div[@id="imgid"]/ul[@class="imglist"]/li[@class="imgitem"]')[0:5]:
            item_final = SightItem()
            item_final['title'] = item['title']
            item_final['lng'] = item['lng']
            item_final['lat'] = item['lat']
            item_final['description'] = item['description']
            item_final['category'] = item['category']
            img_src = option.xpath('a/img/@src').extract_first()
            item['url'] = img_src
            if img_src is None or len(img_src) == 0:
                item['url'] = 'url_null'
                log.msg('img_src is null==============' + img_src, level=log.INFO)
            item_final['url'] = item['url']
            log.msg('img_src in line 61***********' + str(img_src).encode('utf-8') + '; type: %s ' % type(img_src), log.INFO)
            log.msg('img_src: ' + img_src + ' at line 76', level=log.INFO)
            log.msg('run out picture_parse at line 77', level=log.INFO)
            yield item
