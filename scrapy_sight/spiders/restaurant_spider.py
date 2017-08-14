# -*- coding:utf-8 -*-

import scrapy
import re
from hanziconv.hanziconv import HanziConv
from ..items import PoiItem
from ..city import china


class RestaurantSpider(scrapy.Spider):
    name = 'restaurant'
    # allowed_domains = ['google.com', 'googleapis.com', 'baidu.com']
    start_urls = [
        'https://maps.googleapis.com/maps/api/geocode/xml?language=zh_CN&address=上海&key=AIzaSyAw'
        '-IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY']

    def start_requests(self):
        """
        :description
           根据geoapi查询位置坐标       
        :return: 
        """
        for url in self.start_urls:
            for city in china[0:1]:
                item = PoiItem()
                page_num = 0
                print city
                url = 'https://maps.googleapis.com/maps/api/geocode/xml?language=zh_CN&address=%s' \
                      '&key=AIzaSyAw-IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY' % city
                print 'start_url: ' + url
                item['city'] = city
                yield scrapy.Request(url, self.parse, meta={
                    'page_num': page_num,
                    'item': item
                })

    def parse(self, response):
        """
        :description
            根据查询到的坐标进行附近餐厅查找
        :param response: 
        :return: 
        """
        status = response.xpath('//GeocodeResponse/status/text()').extract()
        if len(status) != 0 and status[0] == u'OK':
            item = response.meta['item']
            page_num = response.meta['page_num']
            lat = response.xpath('//geometry/location/lat/text()').extract()[0]
            lng = response.xpath('//geometry/location/lng/text()').extract()[0]
            item['lat'] = lat
            item['lng'] = lng
            # attraction_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml' \
            # '?language=zh_CN&location=%s,
            # ' \ '%s&radius=50000&type=restaurant&keyword=food&key=AIzaSyAw
            # -IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY' % (lat, lng)
            attraction_url = 'https://maps.googleapis.com/maps/api/place/radarsearch/xml?location' \
                             '=%s,' \
                             '%s&radius=50000&type=restaurant&keyword=food&key=AIzaSyAw' \
                             '-IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY' % (lat, lng)
            print 'attraction_url: ' + attraction_url
            yield scrapy.Request(url=attraction_url, callback=self.attraction_parse, meta={
                'page_num': page_num,
                'item': item
            })

    def attraction_parse(self, response):
        """
        :description
            对根据坐标查询到附近的饭店进行解析
        :param response: 
        :return: 
        """
        print 'run into attraction_parse'
        status = response.xpath('//PlaceSearchResponse/status/text()').extract()
        if len(status) != 0 and status[0] == u'OK':
            # page_num = response.meta['page_num']
            counter = 0
            for sel in response.xpath('/PlaceSearchResponse/result'):
                item = response.meta['item']
                place_id = sel.xpath('place_id/text()').extract()
                detail_url = 'https://maps.googleapis.com/maps/api/place/details/xml?language' \
                             '=zh_CN&placeid=%s&key=AIzaSyAw-IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY' % \
                             place_id[0]
                print 'place_id: %s' % place_id
                print 'counter: %s' % counter
                counter += 1
                # print detail_url
                yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={
                    'item': item
                })
            """附近搜索最高只有60结果，现在雷达搜索暂时不用这个"""
            # next_page_token = response.xpath(
            #     '/PlaceSearchResponse/next_page_token/text()').extract()
            # if page_num < 25:
            #     item = response.meta['item']
            #     print 'page_num: {:d}'.format(page_num)
            #     if len(next_page_token) != 0:
            #         page_num += 1
            #         next_page_url =
            # 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml' \
            #                         '?pagetoken=%s&key=AIzaSyAw-IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY'
            # % \
            #                         next_page_token[0]
            #         yield scrapy.Request(next_page_url, callback=self.attraction_parse, meta={
            #             'page_num': page_num,
            #             'item': item
            #         })

    def detail_parse(self, response):
        """
        :description
            对饭店进行逐一解析
        :param response: 
        :return: 
        """
        print 'run into detail_parse'
        item = response.meta['item']
        name = response.xpath('/PlaceDetailsResponse/result/name/text()').extract()
        print 'name: %s' % name[0]
        # if len(name) != 0:
        #     name = name[0]
        item['name'] = name[0]
        address = response.xpath('/PlaceDetailsResponse/result/formatted_address/text()').extract()
        if len(address) != 0:
            address = address[0]
        else:
            address = u'暂无数据'
        item['address'] = address
        mobile = response.xpath(
            '/PlaceDetailsResponse/result/international_phone_number/text()').extract()
        if len(mobile) != 0:
            mobile = mobile[0]
        else:
            mobile = u'暂无数据'
        item['mobile'] = mobile
        open_hours = response.xpath('/PlaceDetailsResponse/result/opening_hours/weekday_text['
                                    '1]/text()').extract()
        if len(open_hours) != 0:
            open_hours = open_hours[0]
            open_hours = open_hours.replace(u'星期一: ', '')
        else:
            open_hours = u'暂无数据'
        item['open_hours'] = open_hours
        photo = response.xpath('/PlaceDetailsResponse/result/photo').extract()
        photo_reference = []
        if len(photo) != 0:
            for sel_photo in response.xpath('/PlaceDetailsResponse/result/photo'):
                result = sel_photo.xpath('photo_reference/text()').extract()[0]
                photo_reference.append(result)
        else:
            photo_reference.append(u'暂无数据')
        item['photo_reference'] = photo_reference
        comment = []
        review = response.xpath('/PlaceDetailsResponse/result/review').extract()
        if len(review) != 0:
            for sel_review in response.xpath('/PlaceDetailsResponse/result/review'):
                result = sel_review.xpath('text/text()').extract()
                if len(result) != 0:
                    comment.append(result[0])
        else:
            comment.append(u'暂无数据')
        item['comment'] = comment
        kg_search_url = 'https://kgsearch.googleapis.com/v1/entities:search?query=%s&key=AIzaSyAw' \
                        '-IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY&limit=1&indent=True&languages' \
                        '=zh_CN' % item['name']
        print 'kg_search_url: ' + kg_search_url
        yield scrapy.Request(url=kg_search_url, callback=self.kg_search_parse, meta={
            'item': item
        })

    def kg_search_parse(self, response):
        """
        :description
            对饭店名字进行知识图谱
        :param response: 
        :return: 
        """
        item = response.meta['item']
        result = response.body
        description = re.findall(r'"articleBody": (.*)?,', result)
        if len(description) != 0:
            description = HanziConv.toSimplified(description[0])
        else:
            description = u'暂无数据'
        item['description'] = description
        subtitle = re.findall(r'"name":(.*)?,', result)
        if len(subtitle) != 0:
            subtitle = HanziConv.toSimplified(subtitle[0])
        else:
            subtitle = u'暂无数据'
        item['subtitle'] = subtitle
        baike_url = 'https://baike.baidu.com/item/%s' % item['name']
        yield scrapy.Request(baike_url, callback=self.baike_parse, meta={
            'item': item
        })

    def baike_parse(self, response):
        item = response.meta['item']
        list_result = response.css('.basicInfo-item.name').extract()
        """这是对某个特色标签处理"""
        recommend = u'暂无数据'
        people_average = u'暂无数据'
        if len(list_result) != 0:
            for sel in response.css('.basicInfo-item.name'):
                result = sel.extract()
                # print result
                name = sel.xpath('text()').extract()[0]
                if name == u'特色菜':
                    print name
                    index = list_result.index(result)
                    value_result = response.css('.basicInfo-item.value')[index].extract()
                    recommend = re.sub(r'<[^>]+>', '', value_result).strip()
                if name == u'人均价格':
                    index = list_result.index(result)
                    value_result = response.css('.basicInfo-item.value')[index].extract()
                    people_average = re.sub(r'<[^>]+>', '', value_result).strip()
                if name == u'营业时间':
                    index = list_result.index(result)
                    value_result = response.css('.basicInfo-item.value')[index].extract()
                    open_hours = re.sub(r'<[^>]+>', '', value_result).strip()
                    item['open_hours'] = open_hours
        item['people_average'] = people_average
        item['recommend'] = recommend
        description = response.css('.lemma-summary').extract()
        if len(description) != 0:
            description = re.sub(r'<[^>]+>', '', description[0]).strip()
            item['description'] = description
        food_series = u'暂无数据'
        recommend_food = []
        div_result = response.css('.content .main-content div').extract()
        for div_list in response.css('.content .main-content div'):
            h_result = div_list.css('.para-title.level-2').extract()
            if len(h_result) != 0:
                for para_title in div_list.css('.para-title.level-2'):
                    type_name = para_title.css('.title-text::text').extract()
                    for i in type_name:
                        if i == u'餐馆类型':
                            food_series_div_index = div_result.index(h_result[0]) + 1
                            food_series = div_result[food_series_div_index]
                            food_series = re.sub(r'<[^>]+>', '', food_series).strip()
                        if i == u'推荐菜':
                            for td_list in response.css('.main-content table.table-view tr td'):
                                td_result = td_list.extract()
                                text_result = re.sub(r'<[^>]+>', '', td_result).strip()
                                recommend_food.append(text_result)
        if len(recommend_food) == 0:
            recommend_food.append(u'暂无数据')
        item['recommend_food'] = recommend_food
        item['food_series'] = food_series
        yield {
            'name': item['name'],
            'address': item['address'],
            'mobile': item['mobile'],
            'city': item['city'],
            'open_hours': item['open_hours'],
            'description': item['description'],
            'lat': item['lat'],
            'lng': item['lng'],
            'subtitle': item['subtitle'],
            'photo_reference': item['photo_reference'],
            'comment': item['comment'],
            'recommend': item['recommend'],
            'people_average': item['people_average'],
            'food_series': item['food_series'],
            'recommend_food': item['recommend_food']
        }
