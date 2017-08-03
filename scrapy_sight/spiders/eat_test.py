# -*- coding: utf-8 -*-

import scrapy
import re


class EatTestSpider(scrapy.Spider):
    name = 'eat'
    allowed_domains = ['ctrip.com']
    start_urls = ["http://you.ctrip.com/food/chiangmai209/10378270.html"]

    # /html/body/div[4]/div/div[1]/div[3]/div[1]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        description = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]').extract()[0]  # 描述
        pattern = re.compile(r'<[^>]+>', re.S)
        description = pattern.sub('', description).strip()
        people_averaged = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[1]/span[2]/em/text()').extract()[0]
        # people_averaged = pattern.sub('', people_averaged).strip()
        special_food = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[2]/p').extract()[0]  # 食物
        special_food = pattern.sub('', special_food).strip().replace(' ', '')
        mobile = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[3]/span[2]/text()').extract()[0]  # 电话
        address = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[4]/span[2]/text()').extract()[0]  # 地址
        open_time = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[5]/span[2]/text()').extract()[0]  # 营业时间
        # print 'description: %s,\n special_food: %s,\n mobile: %s,\n address: %s,\n open_time: %s\n people_averaged: %s' % (description,
        #                                                                                              special_food,
        #                                                                                              mobile, address,
        #                                                                                              open_time, people_averaged)
        print people_averaged
