# -*- coding:utf-8 -*-

import scrapy
import re
from hanziconv.hanziconv import HanziConv
from ..items import PoiItem


class ShoppingSpider(scrapy.Spider):
    page_num = 0
    name = 'shopping'
    allowed_domains = ['google.com', 'googleapis.com']
    start_urls = ['https://maps.googleapis.com/maps/api/geocode/xml?language=zh_CN&address=上海&key'
                  '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k']

    def start_requests(self):
        for url in self.start_urls:
            item = PoiItem()
            city = u'上海'
            url = 'https://maps.googleapis.com/maps/api/geocode/xml?language=zh_CN&address=%s&key' \
                  '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k' % city
            print 'start_url: ' + url
            item['city'] = city
            yield scrapy.Request(url, self.parse, meta={
                'item': item
            })

    def parse(self, response):
        status = response.xpath('//GeocodeResponse/status/text()').extract()
        if len(status) != 0 and status[0] == u'OK':
            item = response.meta['item']
            lat = response.xpath('//geometry/location/lat/text()').extract()[0]
            lng = response.xpath('//geometry/location/lng/text()').extract()[0]
            item['lat'] = lat
            item['lng'] = lng
            attraction_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=%s,%s&radius=50000&type=shoppingCenter&keyword=shopping&key=' % (lat, lng)
            print 'attraction_url: ' + attraction_url
            yield scrapy.Request(url=attraction_url, callback=self.attraction_parse, meta={
                'item': item
            })

    def attraction_parse(self, response):
        print 'run into attraction_parse'
        status = response.xpath('//PlaceSearchResponse/status/text()').extract()
        if len(status) != 0 and status[0] == u'OK':
            item = response.meta['item']
            for sel in response.xpath('/PlaceSearchResponse/result')[0:1]:
                place_id = sel.xpath('place_id/text()').extract()
                detail_url = 'https://maps.googleapis.com/maps/api/place/details/xml?language=zh_CN&placeid=%s&key' \
                             '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k' % place_id[0]
                print detail_url
                yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={
                    'item': item
                })
            next_page_token = response.xpath('/PlaceSearchResponse/next_page_token/text()').extract()
            if self.page_num < 3:
                print self.page_num
                if len(next_page_token) != 0:
                    self.page_num += 1
                    next_page_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?pagetoken=%s&key=' % \
                                    next_page_token[0]
                    yield scrapy.Request(next_page_url, callback=self.attraction_parse, meta={
                        'item': item
                    })

    def detail_parse(self, response):
        print 'run into detail_parse'
        item = response.meta['item']
        name = response.xpath('/PlaceDetailsResponse/result/name/text()').extract()
        if len(name) != 0:
            name = name[0]
        else:
            name = u'暂无数据'
        item['name'] = name
        address = response.xpath('/PlaceDetailsResponse/result/formatted_address/text()').extract()
        if len(address) != 0:
            address = address[0]
        else:
            address = u'暂无数据'
        item['address'] = address
        mobile = response.xpath('/PlaceDetailsResponse/result/international_phone_number/text()').extract()
        if len(mobile) != 0:
            mobile = mobile[0]
        else:
            mobile = u'暂无数据'
        item['mobile'] = mobile
        open_hours = response.xpath('/PlaceDetailsResponse/result/opening_hours/weekday_text[1]/text()').extract()
        if len(open_hours) != 0:
            open_hours = open_hours[0]
        else:
            open_hours = u'暂无数据'
        item['open_hours'] = open_hours
        kg_search_url = 'https://kgsearch.googleapis.com/v1/entities:search?query=%s&key=&limit=1&indent=True&languages=zh_CN' % name
        print 'kg_search_url: ' + kg_search_url
        yield scrapy.Request(url=kg_search_url, callback=self.kg_search_parse, meta={
            'item': item
        })

    def kg_search_parse(self, response):
        item = response.meta['item']
        result = response.body
        description = re.findall(r'"articleBody": (.*)?,', result)
        if len(description) != 0:
            description = HanziConv.toSimplified(description[0])
        else:
            description = u'暂无数据'
        print 'description: ' + description
        yield {
            'name': item['name'],
            'address': item['address'],
            'mobile': item['mobile'],
            'open_hours': item['open_hours'],
            'description': description
        }
