# -*- coding: utf-8 -*-

import scrapy
import re


class EatTestSpider(scrapy.Spider):
    name = 'shopping'
    allowed_domains = ['ctrip.com']
    start_urls = ["http://you.ctrip.com/shopping/chiangmai209/1356153.html"]

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
        description = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]/div/div/text()').extract()[0]  # 描述
        pattern = re.compile(r'<[^>]+>', re.S)
        description = pattern.sub('', description).strip()
        transport = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[2]/div[1]/div/div').extract()[0]  # 交通信息
        transport = pattern.sub('', transport).strip()
        mobile = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[3]/span[2]').extract()[0]  # 电话
        mobile = pattern.sub('', mobile).strip()
        address = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[1]/span[2]/text()').extract()[0]  # 地址
        address = pattern.sub('', address).strip()
        open_time = response.xpath('/html/body/div[4]/div/div[2]/div[1]/dl/dd').extract()[0]  # 营业时间
        open_time = pattern.sub('', open_time).strip()
        print 'description: %s,\n transport: %s,\n mobile: %s,\n address: %s,\n open_time: %s' % (description,
                                                                                                  transport,
                                                                                                  mobile, address,
                                                                                                  open_time)
