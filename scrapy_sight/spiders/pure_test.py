# -*- coding: utf-8 -*-

import scrapy
import re
from ..items import CtripSightItem


class EatTestSpider1(scrapy.Spider):
    name = 'pure_test'
    allowed_domains = ['ctrip.com']
    start_urls = ["http://you.ctrip.com/place"]

    # /html/body/div[4]/div/div[1]/div[3]/div[1]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        ctripItem = CtripSightItem()
        """国家"""
        # for sel in response.xpath('//*[@id="journals-panel-items"]/dl')[2:3]:
        #     print u'continent: ' + sel.xpath('dt/text()').extract()[0]
        #     ctripItem['continent'] = sel.xpath('dt/text()').extract()[0]
        #     for sec_sel in sel.xpath('dd/ul/li')[0:1]:
        #         print u'area: ' + sec_sel.xpath('strong/text()').extract()[0]
        #         ctripItem['area'] = sec_sel.xpath('strong/text()').extract()[0]
        #         for third_sel in sec_sel.xpath('a')[0:1]:
        #             print u'三级目录: ' + third_sel.xpath('@href').extract()[0]
        #             ctripItem['country'] = third_sel.xpath('@href').extract()[0]
        #             url = 'http://you.ctrip.com' + third_sel.xpath('@href').extract()[0]
        #             print url
        #             yield scrapy.Request(url, meta={
        #                 'item': ctripItem,
        #                 'splash': {
        #                     'endpoint': 'render.html',
        #                     'args': {'wait': 1}
        #                 }
        #             }, callback=self.sight_country_parse)
        """城市"""
        for sel in response.xpath('//*[@id="journals-panel-items"]/dl')[1:2]:
            print u'continent: ' + sel.xpath('dt/text()').extract()[0]
            ctripItem['continent'] = sel.xpath('dt/text()').extract()[0]
            for sec_sel in sel.xpath('dd/ul/li')[0:1]:
                print u'area: ' + sec_sel.xpath('strong/text()').extract()[0]
                ctripItem['area'] = sec_sel.xpath('strong/text()').extract()[0]
                for third_sel in sec_sel.xpath('a')[3:4]:
                    print u'三级目录: ' + third_sel.xpath('@href').extract()[0]
                    ctripItem['country'] = u'国内'
                    ctripItem['city'] = third_sel.xpath('@href').extract()[0]
                    url = 'http://you.ctrip.com' + third_sel.xpath('@href').extract()[0]
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
        url = 'http://you.ctrip.com' + ctripItem['scenic_url']
        yield scrapy.Request(url=url, meta={
            'item': ctripItem,
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 1}
            }
        }, callback=self.scenic_parse)

    def sight_city_parse(self, response):
        """
        :这是对城市进行筛选.
        :param response: 
        :return: 
        """
        ctripItem = response.meta['item']
        for sel in response.css('.ttd_topnav ul li'):  # 一级跳转网站
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
                # if name == u'购物':
                #     shopping = sel.xpath('a/@href').extract()[0]
                #     ctripItem['shopping_url'] = sel.xpath('a/@href').extract()[0]
                #     print 'shopping: ' + shopping
        url = 'http://you.ctrip.com' + ctripItem['food_url']
        print 'sight_city_parse: ' + url
        yield scrapy.Request(url=url, meta={
            'item': ctripItem,
            'splash': {
                'endpoint': 'render.html',
                'args': {'wait': 0.5}
            }
        }, callback=self.more_food_parse)

    def more_food_parse(self, response):
        more_url = response.css('.des_wide .normaltitle .f_14')
        for sel in more_url:
            more_text = sel.css('::text').extract()
            if len(more_text) != 0 and more_text[0] == u'更多餐馆':
                # more_food_url = response.css('.des_wide .normaltitle .f_14::attr(href)').extract()
                more_food_url = sel.css('::attr(href)').extract()
                if len(more_food_url) != 0:
                    url = 'http://you.ctrip.com' + more_food_url[0]
                    print url
                    yield scrapy.Request(url=url, callback=self.specific_food_parse)

    def specific_food_parse(self, response):
        for sel in response.css('.list_wide_mod2 .list_mod2 dt a')[0:1]:
            extract = sel.css('::attr(href)').extract()
            if len(extract) != 0:
                url = 'http://you.ctrip.com' + extract[0]
                print url
                yield scrapy.Request(url=url, callback=self.get_food_parse)

    def get_food_parse(self, response):
        result_description = ''
        for sel1 in response.css('.detailcon div.text_style div, .detailcon '
                                 'div.text_style'):
            description = sel1.extract()
            if len(description) != 0:
                result_description += re.sub(r'[\s]+', '', re.sub(r'<[^>]+>', '',
                                                                  description).strip())
        print ('result_description: ' + result_description)

        for sel in response.css('ul.s_sight_in_list li'):
            text = sel.extract()
            if len(text) != 0:
                title = sel.css('span.s_sight_classic::text').extract()[0]
                content = sel.css('span.s_sight_con').extract()
                strip = re.sub(r'<[^>]+>', '', content[0]).strip().encode('gbk', 'ignore')
                print title
                print strip

    def scenic_parse(self, response):
        """
        :description
                这是在国家里面更多的景点解析
        :param response: 
        :return: 
        """
        ctripItem = response.meta['item']
        more_scenic = response.xpath(
            '/html/body/div[5]/div/div[1]/div[3]/div[1]/div[11]/span/a/@href').extract()
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

    def real_sight_parse(self, response):
        """
        :description
                对城市里面的景点进行遍历
        :param response: 
        :return: 
        """
        print 'run into real_sight_parse'
        ctripItem = response.meta['item']
        for sel in response.xpath(
                '/html/body/div[5]/div/div[1]/div/div[3]/div[@class="list_mod1"]')[0:1]:
            path = sel.xpath('div[@class="rdetailbox"]/dl/dt/a/@href').extract()
            url = 'http://you.ctrip.com' + path[0]
            print 'real_sight_parse: ' + url
            yield scrapy.Request(url, meta={
                'item': ctripItem,
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 1}
                }
            }, callback=self.city_parse)

    def city_parse(self, response):
        """
        :description
            这是对景点的最终解析以及提取信息
        :param response: 
        :return: 
        """
        print 'run into city_parse'
        ctripItem = response.meta['item']
        # "/html/body/div[3]/div[1]/div/div[1]/h1/a/text()"
        title = response.xpath('/html/body/div[3]/div[1]/div/div[1]/h1/a/text()').extract()
        if len(title) != 0:
            title = title[0]
        else:
            title = u'title'
        pattern = re.compile(r'<[^>]+>', re.S)
        highlight = response.xpath(
            '/html/body/div[4]/div/div[1]/div[4]/div[1]/ul/li/text()').extract()  # highlight
        highlight = pattern.sub('', highlight[0])
        ctripItem['scenic_highlight'] = highlight
        description = response.xpath(
            '/html/body/div[4]/div/div[1]/div[4]/div[1]/div[1]/div').extract()  # description
        description = pattern.sub('', description[0]).strip()
        ctripItem['scenic_description'] = description
        address = response.xpath('//*[@class="s_sight_infor"]/p/text()').extract()[0]  # address
        address = pattern.sub('', address).strip()[3:]
        ctripItem['scenic_address'] = address
        for sel in response.xpath('//*[@class="s_sight_in_list"]/li'):
            tel = sel.xpath('span[@class="s_sight_classic"]/text()').extract()[0]
            if tel == u'\u7535\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\u8bdd\uff1a':  # 电        话：
                mobile = sel.xpath('span[@class="s_sight_con"]/text()').extract()[0]
                mobile = pattern.sub('', mobile).strip()
                ctripItem['scenic_mobile'] = mobile
            else:
                ctripItem['scenic_mobile'] = u'无信息'
        ticket = u'无信息'
        for sel in response.xpath('//*[@class="s_sight_infor"]/dl'):
            sel_open_time = sel.xpath('dt/text()').extract()[0]
            if sel_open_time == u'\u5f00\u653e\u65f6\u95f4\uff1a':
                open_time = sel.xpath('dd/text()').extract()[0]
            if sel_open_time == u'\u95e8\u7968\u4fe1\u606f\uff1a':
                ticket = sel.xpath('dd/text()').extract()
                if len(ticket) == 0:
                    ticket = u'无信息'
                    ctripItem['scenic_ticket'] = ticket
                else:
                    ticket = pattern.sub('', ticket[0])
                    ctripItem['scenic_ticket'] = ticket
        advice_time = u'无信息'
        for sel in response.xpath('//*[@class="s_sight_in_list"]/li'):
            sel_advice_time = sel.xpath('span[@class="s_sight_classic"]/text()').extract()[0]
            if sel_advice_time == u'\u6e38\u73a9\u65f6\u95f4\uff1a':  # 游玩时间：
                advice_time = sel.xpath('span[@class="s_sight_con"]/text()').extract()[0]
                advice_time = pattern.sub('', advice_time).strip()
                ctripItem['scenic_advice_time'] = advice_time
        # print 'highlight: %s\n description: %s\n address: %s\n mobile: %s\n open_time: %s\n
        # adivce_time: %s\n
        # ticket: ' \ '%s' % ( highlight, description, address, mobile, open_time, advice_time,
        # ticket)
        yield {
            'title': title,
            'description': description,
            'ticket': ticket,
            'advice_time': advice_time,
            'mobile': mobile,
            'address': address,
            'open_time': open_time,
            'continent': ctripItem['continent'],
            'area': ctripItem['area'],
            'country': ctripItem['country'],
            'city.py': ctripItem['city.py']
        }
