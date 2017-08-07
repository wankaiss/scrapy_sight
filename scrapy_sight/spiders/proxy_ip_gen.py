# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import SightItem
from ..items import ProxyIp


class TestSpider(scrapy.Spider):
    name = 'proxy_ip'
    allowed_domains = ['xicidaili.com']
    start_urls = ["http://www.xicidaili.com/nt"]

    def parse(self, response):
        i = 0
        proxy = ProxyIp()
        for sel in response.xpath('//tr'):
            ip = sel.xpath('td[2]/text()').extract_first()
            port = sel.xpath('td[3]/text()').extract_first()

            # item = SightItem()
            # item['url'] = result
            # result = str(result)
            # result = result.replace('<a\s*>', '')
            print ('{"ip_port": "%s:%s", "user_pass": ""},' % (ip, port))
        # yield scrapy.Request(url='http://www.meet99.com/jingdian-jiuzhaigoufengjingqu.html', meta={'item': item}, callback=self.send_img, )

    def send_img(self, response):
        item = response.meta['item']
        item['title'] = 'title'
        {'ip_port': '127.0.0.1:1080', 'user_pass': ''},
        print ('item: %s' % item)