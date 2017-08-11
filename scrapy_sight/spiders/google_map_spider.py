# -*- coding: utf-8 -*-

import scrapy
from hanziconv.hanziconv import HanziConv
import re


# 地图坐标获取
# https://maps.googleapis.com/maps/api/geocode/json?language=zh_CN&address=%E4%B8%8A%E6%B5%B7%E4%B8%AD%E5%BF%83&key=
# 附近查找
#   景点
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=31.2396889,121.4997553&radius=50000&type=TouristAttraction&keyword=attraction&key=
#   购物
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=31.2396889,121.4997553&radius=50000&type=shoppingCenter&keyword=shopping&key=
#   餐厅
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=31.2396889,121.4997553&radius=50000&type=restaurant&keyword=food&key=
#   酒店
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=31.2335024,121.5057629&radius=50000&type=Hotel&keyword=hotel&key=
# 下一页查找
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?pagetoken=CpQCCwEAAFCS8K2flhLlVU4IcH_qp-y8NdvLGTcNHoLqnlw_lrybSqUltPWfTxdWqrdGVRap-KeT1W4sSBN-v17_PFj0Z-orgazinfSc91shspgQnkmPj5VZxZuxDlzS_t_o141WsY9WmEQF922D4JMwXhwl08fDGhQvRQZd6ZjCOi5KKksK4e-1VH5Xtb-fFSqTT6LNBpBUwnHpp1hQQ0ohi0Ixqs2smnGcwCSwAuaL97oBQ6AyMDIcBOI0AKopkkyIYoY50p5bADsq42zf70fBRMz9IoIAxNgiJdwCajlnrQI_Mk0QcOJoXiZi1eG1j0qEpMlcw8yRgsN3hxknAY1SjCmoQj5Le48t1WPXFpiC17uXjEItEhAKmHGWrlINvGARfxTzw3MdGhSs_xQRG4doj4AyJHEFzxXk0cBzjg&key=
# 地点详情
# https://maps.googleapis.com/maps/api/place/details/json?language=zh_CN&placeid
# =ChIJDTwzJEGuEmsRw4ifQGYDkww&key=
# 根据photo-reference查找图片
# https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAApJSns__-0__gPovihJDzG2KFvxMEn11cfihtG8CxrAN774ZEtkJ3upySaqKy6RrPWWY3WIXwF6WBz5TII3g9Zs_XoIV_A0vzwMMyJPRlR18aL46GR4m7mbeOCvI3Jn8kEhBE6b0Lk2I0ocXawDSaP3nsGhQWpiYbcGvmwKL04tcYRD-7kBmX5w&key=
# google geocoding
# https://maps.googleapis.com/maps/api/geocode/json?address=金茂大厦&key=
# 知识图谱
# https://kgsearch.googleapis.com/v1/entities:search?query=taylor+swift&key=&limit=1&indent=True&languages=zh_CN


class google_poi_spder(scrapy.Spider):
    name = 'poi'
    allowed_domains = ['google.com']
    # start_urls = ['https://maps.googleapis.com/maps/api/geocode/xml?language=zh_CN&address=上海中心&key'
    #               '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k']
    start_urls = ['https://kgsearch.googleapis.com/v1/entities:search?query=上海影视乐园&key=&limit=1&indent=True&languages=zh_CN']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.kg_sarch_parse)

    def parse(self, response):
        status = response.xpath('//GeocodeResponse/status/text()').extract()
        print status
        # if len(status) != 0 and status[0] == u'OK':
        lat = response.xpath('//geometry/location/lat/text()').extract()[0]
        lng = response.xpath('//geometry/location/lng/text()').extract()[0]
        """景点"""
        attraction_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=%s,' \
                         '%s&radius=50000&type=TouristAttraction&keyword=attraction&key' \
                         '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k' % (lat, lng)
        print 'attraction_url: ' + attraction_url
        # """购物"""
        # shopping_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=%s,' \
        #                '%s&radius=50000&type=shoppingCenter&keyword=shopping&key' \
        #                '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k' % (lat, lng)
        # print shopping_url
        # # yield scrapy.Request(url=shopping_url, callback=self.shopping_parse)
        # """美食"""
        # restaurant_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=%s,' \
        #                  '%s&radius=50000&type=restaurant&keyword=food&key' \
        #                  '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k' % (lat, lng)
        # print restaurant_url
        # # yield scrapy.Request(url=restaurant_url, callback=
        # """酒店"""
        # hotel_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=%s,' \
        #             '%s&radius=50000&type=Hotel&keyword=hotel&key=' % (
        #                 lat, lng)
        # print hotel_url
        # yield scrapy.Request(hotel_url, callback=self.hotel_parse)
        yield scrapy.Request(attraction_url, self.attraction_parse)

    def attraction_parse(self, response):
        print 'run into attraction_parse'
        status = response.xpath('//PlaceSearchResponse/status/text()').extract()
        print status
        if len(status) != 0 and status[0] == u'OK':
            for sel in response.xpath('/PlaceSearchResponse/result'):
                place_id = sel.xpath('place_id/text()').extract()
                detail_url = 'https://maps.googleapis.com/maps/api/place/details/xml?language=zh_CN&placeid=%s&key' \
                             '=AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k' % place_id[0]
                print detail_url
                yield scrapy.Request(detail_url, self.detail_parse)

    def shopping_parse(self, response):
        ''

    def restaurant_parse(self, response):
        ''

    def hotel_parse(self, response):
        ''

    def detail_parse(self, response):
        print 'run into detail_parse'
        name = response.xpath('/PlaceDetailsResponse/result/name/text()').extract()
        address = response.xpath('/PlaceDetailsResponse/result/formatted_address/text()').extract()
        mobile = response.xpath('/PlaceDetailsResponse/result/international_phone_number/text()').extract()
        open_hours = response.xpath('/PlaceDetailsResponse/result/opening_hours/weekday_text[1]/text()').extract()
        kg_search_url = 'https://kgsearch.googleapis.com/v1/entities:search?query=%s&key=&limit=1&indent=True&languages=zh_CN' % name[0]
        print kg_search_url
        print name, address, mobile, open_hours
        yield scrapy.Request(kg_search_url, callback=self.kg_sarch_parse)

    def kg_sarch_parse(self, response):
        result = response.body
        description = re.findall(r'"articleBody": (.*)?,', result)
        description = HanziConv.toSimplified(description[0])
        print description


if __name__ == '__main__':
    ''
    # detail_url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJM6TkgBpwsjURBfml8nNcnMM&key='
