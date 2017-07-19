# -*- coding: utf-8 -*-
import scrapy
from ..items import SightItem
import uuid


class SightSpider(scrapy.Spider):

    name = 'sight'
    allowed_domains = ['meet99.com']
    start_urls = ["http://www.meet99.com/lvyou"]

    def parse(self, response):
        i = 0
        for sel in response.xpath('//ul[@id="tiles"]//li[@class="box"]'):
            item = SightItem()
            deep_url = sel.xpath('div[@class="img"]/a/@href').extract_first()
            src_url = sel.xpath('div[@class="img]/img/@src"]').extract_first()
            if src_url is None:
                src_url = ''
            item['url'] = src_url
            url = response.urljoin(deep_url)
            print('deep_url: %s, src_url: %s' % (url, src_url))
            i += 1
            yield scrapy.Request(url, meta={'item': item}, callback=self.content_parse)

    def content_parse(self, response):
        item = response.meta['item']
        str1 = response.xpath('//*[@id="jdleft"]/div[2]/div/div[2]/div[1]/text()[1]').extract_first()
        if str1 is None:
            str1 = ''
        title = response.xpath('//*[@id="pageLocation"]/div/a[3]/text()').extract_first()
        if title is None:
            title = ''
        category = response.xpath('//*[@id="pageLocation"]/div[1]/a[2]/text()').extract_first()
        if category is None:
            category = ''
        item['description'] = str1
        item['title'] = title
        item['category'] = category
        item['id'] = uuid.uuid4()
        item['lat'] = ''
        item['lon'] = ''
        print ('str: %s' % str1)
        yield item
