# -*- coding: utf-8 -*-
import scrapy
from ..items import SightItem


class SoloSpider(scrapy.Spider):
    name = 'solocrawl'
    allowed_domains = ['baidu.com']
    start_urls = ["https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E6%97%85%E6%B8%B8%E6%99%AF%E7%82%B9"]

    def parse(self, response):
        i = 0
        for sel in response.xpath('//*[@class="content-wrapper"]/div[1]/div[2]/div'):
            item = SightItem()
            class_type = sel.xpath('@class').extract()
            # print ('result: %s, i %d' % (result, i))
            # if len(class_type) != 0 and class_type[0] == u'para-title level-2':
            #     category = sel.xpath('h2/text()').extract_first()
            #     item['category'] = category
            #     print ('title_level_2: %s, i=: %d' % (category, i))
            #
            # if len(class_type) != 0 and class_type[0] == u'para-title level-3':
            #     title = sel.xpath('h3/text()').extract_first()
            #     item['title'] = title
            #     print ('title_level_3: %s, i=: %d' % (title, i))

            if len(class_type) != 0 and class_type[0] == u'para':
                description = sel.xpath('text()').extract()
                str = ''
                for descrip in description:
                    i += 1
                    str += descrip
                    print ('str: %s, ==================%d' % (str, 1))
