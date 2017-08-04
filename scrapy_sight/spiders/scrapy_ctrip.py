# -*- coding: utf-8 -*-
import scrapy
import re


class CtripSpider(scrapy.Spider):
    global base_url
    base_url = 'http://you.ctrip.com'
    name = 'ctrip'
    allowed_domains = ['ctrip.com']
    start_urls = ["http://you.ctrip.com/place"]

    # http://you.ctrip.com/place/ -- 攻略地点

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        """
        :description
                place地方
        :param response: 
        :return: 
        """
        description = response.xpath('//*[@id="journals-panel-items"]/dl[3]/dd/ul/li[1]/a[1]/@href').extract()
        # pattern = re.compile(r'<[^>]+>', re.S)
        if len(description) != 0:
            path = description[0]
            url_path = base_url + path
        # description = pattern.sub('', description[0])
        #     print url
            yield scrapy.Request(url=url_path, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            }, callback=self.place_parse)

    def place_parse(self, response):
        """
        :description
                区域选择
        :param response: 
        :return: 
        """
        path = response.xpath('/html/body/div[4]/div/div/ul/li[5]/a/@href').extract()
        if len(path) != 0:
            url_path = base_url + path[0]
            print url_path
            yield scrapy.Request(url=url_path, callback=self.sight_parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def sight_parse(self, response):
        """
        :description
                泰国旅游景点
        :param response: 
        :return: 
        """
        path = response.xpath('/html/body/div[5]/div/div[2]/div[3]/div[2]/div[11]/span/a/@href').extract()
        if len(path) != 0:
            url_path = base_url + path[0]
            print 'sight_parse: ' + url_path
            yield scrapy.Request(url=url_path, callback=self.single_sight_parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def single_sight_parse(self, response):
        """
        :description
                泰国各地景点
        :param response: 
        :return: 
        """
        path = response.xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[1]/dl/dt/a/@href').extract()
        url_path = base_url + path[0]
        print 'single_sight_parse: ' + url_path
        yield scrapy.Request(url=url_path, callback=self.real_sight_parse, meta={
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 0.5}
            }
        })

    def real_sight_parse(self, response):
        """
        :description
                泰国单一景点
        :param response: 
        :return: 
        """
        path = response.xpath('/html/body/div[4]/div/div/ul/li[5]/a/@href').extract()
        url_path = base_url + path[0]
        print 'real_sight_parse: ' + url_path
        yield scrapy.Request(url=url_path, callback=self.sight_seeing_parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def sight_seeing_parse(self, response):
        """
        :description
                清迈所有景点
        :param response: 
        :return: 
        """
        path = response.xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/div[1]/div[2]/dl/dt/a/@href').extract()
        url_path = base_url + path[0]
        print 'sight_seeing_parse: ' + url_path
        yield scrapy.Request(url=url_path, callback=self.sight_into_parse, meta={
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 0.5}
            }
        })

    def sight_into_parse(self, response):
        """
        :description 
                详细景点
                /html/body/div[3]/div/div[1]/div[4]/div[1]/ul/li # 亮点
                /html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div # 描述
        :param response: 
        :return: 
        """
        highlight = response.xpath('/html/body/div[3]/div/div[1]/div[4]/div[1]/ul/li/text()').extract()  # 亮点
        description = response.xpath('/html/body/div[4]/div/div[1]/div[4]/div[2]/div[2]/div').extract()  # 描述
        information = response.xpath('/html/body/div[4]/div/div[2]/div[1]').extract()
        print 'highlight: %s; description: %s; information: %s' % (highlight, description, information)
