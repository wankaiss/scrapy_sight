# -*- coding: utf-8 -*-

import scrapy
import re
from ..items import CtripSightItem


class EatTestSpider1(scrapy.Spider):
    name = 'pure_test01'
    allowed_domains = ['ctrip.com']
    start_urls = ["http://you.ctrip.com/place/lijiang31.html"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                # 'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        ctripItem = CtripSightItem()
        """国家"""
        # for sel in response.xpath('//*[@id="journals-panel-items"]/dl')[1:3]:
        #     print u'continent: ' + sel.xpath('dt/text()').extract()[0]
        #     ctripItem['continent'] = sel.xpath('dt/text()').extract()[0]
        #     for sec_sel in sel.xpath('dd/ul/li')[0:1]:
        #         print u'area: ' + sec_sel.xpath('strong/text()').extract()[0]
        #         ctripItem['area'] = sec_sel.xpath('strong/text()').extract()[0]
        #         for third_sel in sec_sel.xpath('a')[0:1]:
        #             print u'三级目录: ' + third_sel.xpath('@href').extract()[0]
        #             ctripItem['country'] = third_sel.xpath('@href').extract()[0]
        #             url = 'http://you.ctrip.com' + third_sel.xpath('@href').extract()[0]
        #             yield scrapy.Request(url, meta={
        #                 'item': ctripItem,
        #                 'splash': {
        #                     'endpoint': 'render.html',
        #                     'args': {'wait': 0.5}
        #                 }
        #             }, callback=self.sight_country_parse)
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
                    ctripItem['city'] = third_sel.xpath('@href').extract()[0]
                    url = 'http://you.ctrip.com' + third_sel.xpath('@href').extract()[0]
                    print url
                    yield scrapy.Request(url, meta={
                        'item': ctripItem,
                        'splash': {
                            'endpoint': 'render.html',
                            'args': {'wait': 0.5}
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
        food = None
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
                print 'food: ' + food
            if name == u'购物':
                shopping = sel.xpath('a/@href').extract()[0]
                ctripItem['shopping_url'] = sel.xpath('a/@href').extract()[0]
                print 'shopping: ' + shopping
        if food is not None:
            url = 'http://you.ctrip.com' + food
            print url
            yield scrapy.Request(url=url, meta={
                'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            }, callback=self.scenic_parse)
        else:
            print 'food path is None'

    def sight_city_parse(self, response):
        """
        :description
                这是对城市进行筛选
        :param response: 
        :return: 
        """
        print 'run into sight_city_parse'
        ctripItem = response.meta['item']
        food = None
        for sel in response.xpath('/html/body/div[4]/div/div/ul/li'):  # 一级跳转网站
            name = sel.xpath('a/text()').extract()
            if len(name) != 0:
                name = name[0]
                print name
            if name == u'景点':
                scenic = sel.xpath('a/@href').extract()[0]
                # ctripItem['scenic_url'] = sel.xpath('a/@href').extract()[0]
                print 'scenic: ' + scenic
            if name == u'美食':
                food = sel.xpath('a/@href').extract()[0]
                print 'food: ' + food
            if name == u'购物':
                shopping = sel.xpath('a/@href').extract()[0]
                # ctripItem['shopping_url'] = sel.xpath('a/@href').extract()[0]
                print 'shopping: ' + shopping
        if food is not None:
            url = 'http://you.ctrip.com' + food
            print url
            yield scrapy.Request(url=url, meta={
                'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            }, callback=self.restaurant_parse)
        else:
            print 'food path is None'

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
        more_scenic = response.xpath('/html/body/div[5]/div/div[1]/div[4]/div[1]/div[11]/span/a/@href').extract()
        #  购物
        # more_scenic = response.xpath('/html/body/div[5]/div/div[1]/div[1]/div[1]/div[11]/span/a/@href').extract()
        yield scrapy.Request(url='http://you.ctrip.com' + more_scenic[0], meta={
            'item': ctripItem,
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 0.5}
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
                ctripItem['city'] = city[0]
            else:
                ctripItem['city'] = u'无数据'
            print 'path: ' + path
            url = 'http://you.ctrip.com' + path
            yield scrapy.Request(url=url, meta={
                'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            }, callback=self.restaurant_parse)

    def restaurant_parse(self, response):
        ctripItem = response.meta['item']
        path = response.xpath('/html/body/div[5]/div/div[1]/div[3]/div[1]/span/a/@href').extract()
        if len(path) != 0:
            url = 'http://you.ctrip.com' + path[0]
            print url
            yield scrapy.Request(url, callback=self.restaurant_list_parse, meta={
                'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def restaurant_list_parse(self, response):
        ctripItem = response.meta['item']
        for sel in response.xpath('/html/body/div[5]/div/div[1]/div/div[3]/div')[0:1]:
            path = sel.xpath('div[@class="rdetailbox"]/dl/dt/a/@href').extract()
            print 'run into restaurant_list_parse'
            print path
            if len(path) != 0:
                url = 'http://you.ctrip.com' + path[0]
                print url
                yield scrapy.Request(url, callback=self.specific_restaurant_parse, meta={
                    'item': ctripItem,
                    'splash': {
                        'endpoint': 'render.html',
                        'args': {'wait': 0.5}
                    }
                })

    def specific_restaurant_parse(self, response):
        ctripItem = response.meta['item']
        pattern = re.compile(r'<[^>]+>', re.S)
        title = response.xpath('/html/body/div[3]/div[1]/div/div[1]/h1/text()').extract()
        description = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]').extract()  # 描述
        if len(description) != 0:
            description = pattern.sub('', description[0]).strip()
        else:
            description = u'无数据'
        people_averaged = response.xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li[1]/span[1]/em/text()').extract()[0]
        # people_averaged = pattern.sub('', people_averaged).strip()
        special_food = response.xpath('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[1]/p').extract()[0]  # 食物
        special_food = pattern.sub('', special_food).strip().replace(' ', '')
        mobile = response.xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li[3]/span[1]/text()').extract()[0]  # 电话
        address = response.xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li[4]/span[1]/text()').extract()[0]  # 地址
        open_time = response.xpath('/html/body/div[4]/div/div[1]/div[1]/ul/li[5]/span[1]/text()').extract()[0]  # 营业时间
        # print 'description: %s,\n special_food: %s,\n mobile: %s,\n address: %s,\n open_time: %s\n people_averaged:
        #  %s' % ( description, special_food, mobile, address, open_time, title)
        yield {
            'title': title[0],
            'description': description,
            'people_averaged': people_averaged,
            'special_food': special_food,
            'mobile': mobile,
            'address': address,
            'open_time': open_time,
            'continent': ctripItem['continent'],
            'area': ctripItem['area'],
            'country': ctripItem['country'],
            'city': ctripItem['city']
        }

if __name__ == '__main__':
    print
