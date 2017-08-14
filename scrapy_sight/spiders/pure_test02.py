# -*- coding: utf-8 -*-

import scrapy
import re
from ..items import CtripSightItem


class EatTestSpider1(scrapy.Spider):
    name = 'pure_test02'
    allowed_domains = ['ctrip.com']
    start_urls = ["http://you.ctrip.com/place"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        ctripItem = CtripSightItem()
        """国家"""
        for sel in response.xpath('//*[@id="journals-panel-items"]/dl')[1:3]:
            print u'continent: ' + sel.xpath('dt/text()').extract()[0]
            ctripItem['continent'] = sel.xpath('dt/text()').extract()[0]
            for sec_sel in sel.xpath('dd/ul/li')[0:1]:
                print u'area: ' + sec_sel.xpath('strong/text()').extract()[0]
                ctripItem['area'] = sec_sel.xpath('strong/text()').extract()[0]
                for third_sel in sec_sel.xpath('a')[0:1]:
                    print u'三级目录: ' + third_sel.xpath('@href').extract()[0]
                    ctripItem['country'] = third_sel.xpath('@href').extract()[0]
                    url = 'http://you.ctrip.com' + third_sel.xpath('@href').extract()[0]
                    yield scrapy.Request(url, meta={
                        'item': ctripItem,
                        'splash': {
                            'endpoint': 'render.html',
                            'args': {'wait': 1}
                        }
                    }, callback=self.sight_country_parse)
        """城市"""
        for sel in response.xpath('//*[@id="journals-panel-items"]/dl')[1:1]:
            print u'continent: ' + sel.xpath('dt/text()').extract()[0]
            ctripItem['continent'] = sel.xpath('dt/text()').extract()[0]
            for sec_sel in sel.xpath('dd/ul/li')[0:1]:
                print u'area: ' + sec_sel.xpath('strong/text()').extract()[0]
                ctripItem['area'] = sec_sel.xpath('strong/text()').extract()[0]
                for third_sel in sec_sel.xpath('a')[0:1]:
                    print u'三级目录: ' + third_sel.xpath('@href').extract()[0]
                    ctripItem['country'] = u'国内'
                    ctripItem['city.py'] = third_sel.xpath('text()').extract()[0]
                    url = 'http://you.ctrip.com' + third_sel.xpath('@href').extract()[0]
                    print url
                    yield scrapy.Request(url, meta={
                        'item': ctripItem,
                        'splash': {
                            'endpoint': 'render.html',
                            'args': {'wait': 1}
                        }
                    }, callback=self.sight_city_parse)

    def sight_country_parse(self, response):
        """
        @description
                这是对国家进行筛选
        :param response: 
        :return: 
        """
        ctripItem = response.meta['item']
        for sel in response.xpath('/html/body/div[4]/div/div/ul/li'):  # 一级跳转网站
            name = sel.xpath('a/text()').extract()
            if len(name) != 0:
                name = name[0]
            if name == u'景点':
                scenic = sel.xpath('a/@href').extract()[0]
                ctripItem['scenic_url'] = sel.xpath('a/@href').extract()[0]
                print 'scenic: ' + scenic
            if name == u'美食':
                food = sel.xpath('a/@href').extract()[0]
                ctripItem['food_url'] = sel.xpath('a/@href').extract()[0]
                print 'food: ' + food
            if name == u'购物':
                shopping = sel.xpath('a/@href').extract()[0]
                ctripItem['shopping_url'] = sel.xpath('a/@href').extract()[0]
                print 'shopping: ' + shopping
        url = 'http://you.ctrip.com' + ctripItem['shopping_url']
        print url
        yield scrapy.Request(url=url, meta={
            'item': ctripItem,
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 1}
            }
        }, callback=self.scenic_parse)

    def scenic_parse(self, response):
        """
        :description
                这是在国家里面更多的美食解析
        :param response: 
        :return: 
        """
        ctripItem = response.meta['item']
        #  景点
        # more_scenic = response.xpath('/html/body/div[5]/div/div[1]/div[3]/div[1]/div[11]/span/a/@href').extract()
        # 美食
        # more_scenic = response.xpath('/html/body/div[5]/div/div[1]/div[4]/div[1]/div[11]/span/a/@href').extract()
        #  购物
        more_scenic = response.xpath('/html/body/div[5]/div/div[1]/div[1]/div[1]/div[11]/span/a/@href').extract()
        yield scrapy.Request(url='http://you.ctrip.com' + more_scenic[0], meta={
            'item': ctripItem,
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 1}
            }
        }, callback=self.country_list_parse)

    def country_list_parse(self, response):
        """
        :description
                承接scenic_parse里面更多的内容，显示国家景点列表
        :param response: 
        :return: 
        """
        ctripItem = response.meta['item']
        for sel in response.xpath('/html/body/div[5]/div/div[1]/div/div[1]/div')[0:1]:  # 遍历国家里面城市列表
            path = sel.xpath('div/a/@href').extract()[0]
            # '/html/body/div[5]/div/div[1]/div/div[1]/div[1]/dl/dt/a'
            city = sel.xpath('dl/dt/a/text()').extract()
            if len(city) != 0:
                ctripItem['city.py'] = city[0]
            else:
                ctripItem['city.py'] = u'无数据'
            print 'path: ' + path
            url = 'http://you.ctrip.com' + path
            yield scrapy.Request(url=url, meta={
                'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 1}
                }
            }, callback=self.sight_city_parse)

    def sight_city_parse(self, response):
        """
        :description
                这是对城市进行筛选
        :param response: 
        :return: 
        """
        print 'run into sight_city_parse'
        ctripItem = response.meta['item']
        for sel in response.xpath('/html/body/div[4]/div/div/ul/li'):  # 一级跳转网站
            # '/html/body/div[4]/div/div/ul/li[1]'
            name = sel.xpath('a/text()').extract()
            # print name
            if len(name) != 0:
                name = name[0]
            if name == u'景点':
                scenic = sel.xpath('a/@href').extract()[0]
                ctripItem['scenic_url'] = scenic
                print 'scenic: ' + scenic
            if name == u'美食':
                food = sel.xpath('a/@href').extract()[0]
                ctripItem['food_url'] = food
                print 'food: ' + food
            if name == u'购物':
                shopping = sel.xpath('a/@href').extract()[0]
                ctripItem['shopping_url'] = shopping
                # '/html/body/div[4]/div/div/ul/li[7]/a'
                print 'shopping: ' + shopping
                # print 'shopping: ' + ctripItem['shopping_url']
        url = 'http://you.ctrip.com' + shopping
        print 'sight_city_parse: ' + url
        yield scrapy.Request(url=url, meta={
            'item': ctripItem,
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 1}
            }
        }, callback=self.shopping_parse)

    def shopping_parse(self, response):
        """
        :description
                更多购物地点
        :param response: 
        :return: 
        """
        ctripItem = response.meta['item']
        path = response.xpath('/html/body/div[5]/div/div[1]/div[3]/div[1]/span/a/@href').extract()
        if len(path) != 0:
            path = response.xpath('/html/body/div[5]/div/div[1]/div[3]/div[1]/span/a/@href').extract()
        else:
            path = response.xpath('/html/body/div[5]/div/div[1]/div[4]/div[1]/span/a/@href').extract()
        # '/html/body/div[5]/div/div[1]/div[4]/div[1]/span/a'
        if len(path) != 0:
            url = 'http://you.ctrip.com' + path[0]
            print url
            yield scrapy.Request(url=url, meta={
                'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 1}
                }
            }, callback=self.shopping_list_parse)

    def shopping_list_parse(self, response):
        print 'run into shopping_list_parse'
        ctripItem = response.meta['item']
        selectors = response.xpath('/html/body/div[5]/div/div[1]/div/div[4]/div[@class="list_mod1"]')
        if len(selectors) != 0:
            selectors = response.xpath('/html/body/div[5]/div/div[1]/div/div[4]/div[@class="list_mod1"]')
        else:
            selectors = response.xpath('/html/body/div[5]/div/div[1]/div/div[3]/div[@class="list_mod1"]')
        for sel in selectors[0:1]:
            path = sel.xpath('div[@class="rdetailbox"]/dl/dt/a/@href').extract()
            print 'path: ' + path[0]
            if len(path) != 0:
                url = 'http://you.ctrip.com' + path[0]
                print url
                yield scrapy.Request(url=url, meta={
                    'item': ctripItem,
                    'splash': {
                        'endpoint': 'render.html',
                        'args': {'wait': 1}
                    }
                }, callback=self.specific_shopping_parse)

    def specific_shopping_parse(self, response):
        print 'run into specific_shopping_parse'
        ctripItem = response.meta['item']
        title = response.xpath('/html/body/div[3]/div[1]/div/div[1]/h1/a/text()').extract()
        if len(title) != 0:
            title = title[0]
        else:
            title = u'title'
        description = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]/div/div/text()').extract()  # 描述
        if len(description) != 0:
            description = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]/div/div/text()').extract()  # 描述
        else:
            description = response.xpath('/html/body/div[4]/div/div[1]/div[4]/div[1]/div[1]/div').extract()
        pattern = re.compile(r'<[^>]+>', re.S)
        description = pattern.sub('', description[0]).strip()
        transport = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]/div/div').extract()  # 交通信息
        if len(transport) != 0:
            transport = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]/div/div').extract()  # 交通信息
        else:
            transport = response.xpath('/html/body/div[4]/div/div[1]/div[4]/div[1]/div[1]/div/div').extract()
        if len(transport) != 0:
            transport = pattern.sub('', transport[0]).strip()
        else:
            transport = u'暂无交通信息'
        mobile = response.xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li[3]/span[1]').extract()[0]  # 电话
        mobile = pattern.sub('', mobile).strip()
        address = response.xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li[1]/span[1]/text()').extract()[0]  # 地址
        address = pattern.sub('', address).strip()
        open_time = response.xpath('/html/body/div[4]/div/div[1]/div[1]/dl/dd').extract()[0]  # 营业时间
        open_time = pattern.sub('', open_time).strip()
        yield {
            'title': title,
            'description': description,
            'transport': transport,
            'mobile': mobile,
            'address': address,
            'open_time': open_time,
            'continent': ctripItem['continent'],
            'area': ctripItem['area'],
            'country': ctripItem['country'],
            'city.py': ctripItem['city.py']
        }


if __name__ == '__main__':
    # title = u"\u77f3\u9505\u6e14\u15aa\u5c71\u73cd\u9986"
    text01 = unichr('\u77f3\u9505\u6e14\u15aa\u5c71\u73cd\u9986')
    # width = half1full_width(unicode01)
    # print title
