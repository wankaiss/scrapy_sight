# -*- coding: utf-8 -*-
import scrapy
from ..items import SightItem
import re
from ..geo_api import baidu_geo_api, google_geo_api
from ..landmark import Editors_pick4
from pypinyin import lazy_pinyin
from scrapy import log
import urllib
from ..settings import PAGE_NUM
from ..picture_utils import save_img, jpg_test, img_resize


class SightSpider(scrapy.Spider):

    def __init__(self):
        self.id_num = 9000040001

    name = 'sight'
    allowed_domains = ['baidu.com']
    start_urls = ["http://image.baidu.com"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        for build in Editors_pick4:
            item = SightItem()
            log.msg('build: ' + build, level=log.INFO)
            if baidu_geo_api(build.encode('utf-8')) is not None:
                lng, lat = baidu_geo_api(build.encode('utf-8'))
            else:
                lng, lat = 1, 1
            item['lng'] = lng
            item['lat'] = lat
            item['id_num'] = self.id_num
            self.id_num += 1L
            item['category'] = u'地标建筑'
            item['title'] = build.encode('utf-8')
            pinyin = lazy_pinyin(build)
            item['pinyin'] = ''.join(pinyin).upper()
            if lng == 1 or lat == 1:
                log.msg('no landmark found: ' + 'at line 36,' + build, level=log.INFO)
                continue
            baike_url = 'https://baike.baidu.com/item/%s' % build
            yield scrapy.Request(baike_url, meta={'item': item}, callback=self.content_parse)

    def content_parse(self, response):
        log.msg('run into content_parse at line 40', level=log.INFO)
        item = response.meta['item']
        result = response.xpath(
            '//div[@class="main-content"]/div[@class="lemma-summary"]/div[@class="para"]').extract()  # 大厦描述
        if len(result) != 0:
            pattern = re.compile(r'<[^>]+>', re.S)
            description = pattern.sub('', result[0]).encode('utf-8')
        else:
            description = 'description_null'
        item['description'] = description
        picture_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&ic=0&width=0&height=0' % item[
            'title'].decode('utf-8')
        log.msg('picture_url: ' + picture_url, level=log.INFO)
        log.msg('run out content_parse at line 51', level=log.INFO)
        yield scrapy.Request(picture_url, meta={'item': item,
                                                'splash': {
                                                    'endpoint': 'render.html',
                                                    'args': {'wait': 0.5}
                                                }
                                                }, callback=self.picture_parse)

    def picture_parse(self, response):
        log.msg('run into picture_parse at line 66', level=log.INFO)
        item = response.meta['item']
        host_address = 'http://image.baidu.com'
        path = response.xpath('//*[@id="page"]/a[10]/@href').extract_first()
        url = host_address.encode('utf-8') + path
        page_num = response.xpath('//*[@id="page"]/strong/span/text()').extract_first()
        log.msg('page_num is %s' % page_num, level=log.INFO)
        for option in response.xpath('//div[@id="imgid"]/ul[@class="imglist"]/li[@class="imgitem"]'):
            item_final = SightItem()
            item_final['title'] = item['title']
            item_final['lng'] = item['lng']
            item_final['lat'] = item['lat']
            item_final['description'] = item['description']
            item_final['category'] = item['category']
            img_src = option.xpath('a/@href').extract_first()
            result = re.search(r'.*objurl=(http.*?)&.*', img_src).groups()[0]
            img_src = urllib.unquote(result).encode('utf-8')
            item['url'] = img_src
            print 'img_src: %s ========================****==============' % img_src
            img_url = jpg_test(img_url=img_src)
            print 'function jpg_test img_url is: %s ****************************' % img_url
            # if img_url is not None:
            try:
                print 'id_num: %s' % item['id_num']
                save_img(img_url=img_url, id_num=item['id_num'])
            except TypeError as e:
                log.msg('img url is NoneType in function picture_parse at line 103: {0}'.format(e), level=log.INFO)
            if img_src is None or len(img_src) == 0:
                item['url'] = 'url_null'
                log.msg('img_src is null==============' + img_src, level=log.INFO)
            item_final['url'] = item['url']
            log.msg('img_src in line 61***********' + img_src + '; type: %s ' % type(img_src), log.INFO)
            log.msg('run out picture_parse at line 92', level=log.INFO)
            yield item

        if path and page_num < PAGE_NUM:
            log.msg('***************path**************\r\n' + path, level=log.INFO)
            yield scrapy.Request(url, meta={'item': item,
                                            'splash': {
                                                'endpoint': 'render.html',
                                                'args': {'wait': 0.5}
                                            }
                                            }, callback=self.picture_parse)

            # def next_page_parse(self, response):
