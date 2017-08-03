# -*- coding: utf-8 -*-

import scrapy
import re


class CtripSightSpider(scrapy.Spider):
    name = 'qingmai'
    allowed_domains = ['ctrip.com']
    start_urls = ["http://you.ctrip.com/sight/chiangmai209/8142.html"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        pattern = re.compile(r'<[^>]+>', re.S)
        highlight = response.xpath('/html/body/div[4]/div/div[1]/div[4]/div[1]/ul/li/text()').extract()  # 亮点
        highlight = pattern.sub('', highlight[0])
        description = response.xpath('/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div').extract()  # 描述
        description = pattern.sub('', description[0]).strip()
        address = response.xpath('/html/body/div[4]/div/div[2]/div[1]/p/text()').extract()[0]  # 地址
        address = pattern.sub('', address).strip()
        mobile = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[3]/span[2]').extract()  # 电话
        mobile = pattern.sub('', mobile[0]).strip()
        open_time = response.xpath('/html/body/div[4]/div/div[2]/div[1]/dl/dd').extract()  # 开放时间
        open_time = pattern.sub('', open_time[0])
        advice_time = response.xpath('/html/body/div[4]/div/div[2]/div[1]/ul/li[2]/span[2]').extract()[0]  # 游玩时间
        advice_time = pattern.sub('', advice_time).strip()
        ticket = response.xpath('/html/body/div[4]/div/div[2]/div[1]/dl[2]/dd').extract()
        if len(ticket) == 0:
            ticket = u'无信息'
        else:
            ticket = pattern.sub('', ticket[0])
        # assert isinstance(information, object)
        print 'highlight: %s\n description: %s\n address: %s\n mobile: %s\n open_time: %s\n adivce_time: %s\n ticket: %s' % (highlight, description,
                                                                                          address, mobile, open_time, advice_time, ticket)
        # print ticket