# -*- coding: utf-8 -*-

import scrapy
import re


class RestaurantSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baidu.com']
    start_urls = {
        'https://baike.baidu.com/item/%E9%94%A1%E4%BC%AF%E6%96%B0%E7%96%86%E9%A4%90%E5%8E%85'}

    def start_requests(self):
        """
        :description
           根据geoapi查询位置坐标       
        :return: 
        """
        for url in self.start_urls:
            yield scrapy.Request(url, self.baike_parse)

    def baike_parse(self, response):
        print 'run into baike_parse'
        recommend_food = []
        result = response.css('.content .main-content div').extract()
        for div_list in response.css('.content .main-content div'):
            h_result = div_list.css('.para-title.level-2').extract()
            if len(h_result) != 0:
                for para_title in div_list.css('.para-title.level-2'):
                    type_name = para_title.css('.title-text::text').extract()
                    for i in type_name:
                        if i == u'推荐菜':
                            # print response.css('.main-content table.table-view tr td').extract()
                            for td_list in response.css('.main-content table.table-view tr td'):
                                td_result = td_list.extract()
                                text_result = re.sub(r'<[^>]+>', '', td_result).strip()
                                recommend_food.append(text_result)
        print recommend_food

if __name__ == '__main__':
    list_test = []
    list_test.append('a')
    list_test.append('b')
    list_test.append('c')
    print list_test
