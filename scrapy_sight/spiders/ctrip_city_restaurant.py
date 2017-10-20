# coding: gbk
import re
import scrapy


from scrapy_sight.items import CtripSightItem


class CtripSortedSpider(scrapy.Spider):
    name = 'ctrip_restaurant'
    allowed_domains = ['ctrip.com']
    next_page_city_counter = 0
    next_page_restaurant_counter = 0
    start_urls = ["http://you.ctrip.com/countrysightlist/china110000.html"]

    def start_requests(self):
        for url in self.start_urls:
            self.next_page_city_counter = 0
            self.next_page_city_counter = 0
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for sel in response.css('.list_wide_mod1 .list_mod1')[0:1]:
            result = sel.css('.ttd_nopic100::attr(href)').extract()
            if len(result) != 0:
                url = 'http://you.ctrip.com' + result[0]
                yield scrapy.Request(url, meta={
                    'splash': {
                        'endpoint': 'render.html',
                        'args': {'wait': 0.5}
                    }
                }, callback=self.sight_city_parse)
                next_page = response.css('a.nextpage::attr(href)').extract()
                if len(next_page) != 0 and self.next_page_city_counter < 5:
                    self.next_page_city_counter += 1
                    print self.next_page_city_counter
                    next_page = next_page[0]
                    url = 'http://you.ctrip.com' + next_page
                    yield scrapy.Request(url, callback=self.parse)

    def sight_city_parse(self, response):
        """
        ���ǶԳ�����Ŀ����ɸѡ.
        """
        ctripItem = CtripSightItem()
        for sel in response.css('.ttd_topnav ul li'):  # һ����ת��վ
            name = sel.xpath('a/text()').extract()
            if len(name) != 0:
                name = name[0]
            if name == u'����':
                scenic = sel.xpath('a/@href').extract()[0]
                ctripItem['scenic_url'] = sel.xpath('a/@href').extract()[0]
                print 'scenic: ' + scenic
            if name == u'��ʳ':
                food = sel.xpath('a/@href').extract()[0]
                ctripItem['food_url'] = sel.xpath('a/@href').extract()[0]
                print 'food: ' + food
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
        """
        ���ǶԵ������ʳ��Ŀ����ת����ʳҳ�� 
        """
        more_url = response.css('.des_wide .normaltitle .f_14')
        for sel in more_url:
            more_text = sel.css('::text').extract()
            if len(more_text) != 0 and more_text[0] == u'����͹�':
                more_food_url = sel.css('::attr(href)').extract()
                if len(more_food_url) != 0:
                    url = 'http://you.ctrip.com' + more_food_url[0]
                    print url
                    yield scrapy.Request(url=url, callback=self.specific_food_parse)

    def specific_food_parse(self, response):
        """����ѡ�����͹ݺ��ҳ��"""
        for sel in response.css('.list_wide_mod2 .list_mod2 dt a')[0:1]:  # ���Ե�ʱ��������Ƭʹ��һ������������
            extract = sel.css('::attr(href)').extract()
            if len(extract) != 0:
                url = 'http://you.ctrip.com' + extract[0]
                print url
                yield scrapy.Request(url=url, callback=self.get_food_parse)

                # ���ڵݹ��ѯ�������
                next_page = response.css('a.nextpage::attr(href)').extract()
                if len(next_page) != 0 and self.next_page_restaurant_counter < 5:
                    self.next_page_restaurant_counter += 1
                    print self.next_page_restaurant_counter
                    next_page = next_page[0]
                    url = 'http://you.ctrip.com' + next_page
                    yield scrapy.Request(url, callback=self.specific_food_parse)

    def get_food_parse(self, response):
        """�����ڸ���͹�ҳ����о���ѡ����һ�Ҳ���"""
        destination = ''
        for sel in response.xpath('//div[@class="breadbar_v1 cf"]/ul[1]/li')[2:]:
            result = sel.xpath('a/text()').extract()
            if len(result) != 0:
                destination += result[0] + u'-'
        if len(destination) != 0:
            destination = destination[:len(destination) - 1]
        restaurant_name = response.css('.dest_toptitle h1::text').extract()
        if len(restaurant_name) != 0:
            print('run into if condition')
            restaurant_name = restaurant_name[0]
            print restaurant_name
        else:
            restaurant_name = ''
        result_description = ''
        for sel1 in response.css('.detailcon div.text_style div, .detailcon '
                                 'div.text_style'):
            description = sel1.extract()
            if len(description) != 0:
                result_description += re.sub(r'[\s]+', '', re.sub(r'<[^>]+>', '',
                                                                  description).strip().encode(
                    'gbk', 'ignore'))
        print ('result_description: ' + result_description)

        restaurant_info = {}
        for sel in response.css('ul.s_sight_in_list li'):
            text = sel.extract()
            if len(text) != 0:
                title = sel.css('span.s_sight_classic::text').extract()[0]
                content = sel.css('span.s_sight_con').extract()
                strip = re.sub(r'<[^>]+>', '', content[0]).strip().encode('gbk', 'ignore')
                strip = re.sub(r'[\s]+', '', strip)
                restaurant_info[title] = strip

        for sel in response.css('.s_sight_in_list')[1:]:
            title = sel.css('dt::text').extract()
            if len(title) != 0:
                title = title[0]
                content = sel.css('dd::text').extract()
                content = content[0]
                restaurant_info[title] = content

        yield {
            'description': result_description,
            'category': 'restaurant',
            'restaurant_name': restaurant_name,
            'restaurant_info': restaurant_info,
            'destination': destination
        }
