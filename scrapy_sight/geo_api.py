# -*- coding: utf-8 -*-
import urllib2
import json
from scrapy import log

landmark = [u'上海中心大厦',
            u'周大福中心',
            u'环球金融中心',
            u'环球贸易广场',
            u'紫峰大厦',
            u'京基金融中心',
            u'国际金融中心',
            u'金茂大厦',
            u'国际金融中心二期',
            u'中信广场',
            u'地王大厦',
            u'高雄85大楼',
            u'中环广场',
            u'中国银行大厦',
            u'广晟国际大厦',
            u'赛格广场',
            u'中环中心',
            u'九龙仓国金中心',
            u'德基广场二期',
            u'环球金融中心',
            u'世茂国际广场',
            u'世界贸易中心',
            u'现代传媒中心',
            u'民生银行大厦',
            u'国际贸易中心三期',
            u'江阴空中华西村',
            u'如心广场',
            u'环球都会广场',
            u'九州国际大厦',
            u'河西青奥中心2号楼',
            u'茂业中心A塔',
            u'珠江城大厦',
            u'越秀金融大厦',
            u'东海国际中心E座',
            u'港岛东中心',
            u'茂业城二期',
            u'长富金茂大厦',
            u'地王国际财富中心',
            u'深长城中心',
            u'利通大厦',
            u'安徽省广电新中心',
            u'京基滨河时代',
            u'富力盈凯广场',
            u'环球经贸中心',
            u'恒隆广场',
            u'英利国际金融中心',
            u'世茂洲际酒店',
            u'盛高环球大厦A塔',
            u'明天广场',
            u'天盈广场C3',
            u'东海国际中心D座',
            u'世界贸易中心',
            u'长江中心',
            u'高德置地广场南塔',
            u'信息枢纽大楼',
            u'卓越世纪中心1号楼',
            u'绿地广场会展宾馆',
            u'香港新世界大厦',
            u'金石国际大酒店',
            u'地王国际商会中心',
            u'世茂国际中心',
            u'绿景纪元大厦',
            u'世界贸易大厦',
            u'会德丰国际广场',
            u'天玺A座',
            u'天玺B座',
            u'中华国际中心B座',
            u'时代金融中心',
            u'皇庭·皇岗商务中心',
            u'高速·滨湖时代广场',
            u'广州银行大厦',
            u'交银金融大厦',
            u'普提金国际金融中心',
            u'上海银行大厦',
            u'K11尖沙咀凯悦酒店',
            u'新葡京酒店',
            u'广东电信广场',
            u'特区报业大厦',
            u'国金中心北塔',
            u'嘉里中心二期A座',
            u'盛高环球大厦B塔',
            u'浪高君悦酒店',
            u'浪高会展国际广场D栋',
            u'中银大厦',
            u'和黄地铁广场D栋',
            u'润华国际大厦',
            u'浙江财富金融中心西塔',
            u'宇洋中央金座',
            u'环球航运广场',
            u'擎天半岛A座',
            u'工商银行大厦',
            u'嘉陵帆影国际经贸中心一期',
            u'新世纪广场A楼',
            u'朗豪坊',
            u'正佳东方国际广场',
            u'江苏电网调度中心大厦',
            u'富力盈耀广场',
            u'晓庐',
            u'平安大厦',
            u'君临天下']


def google_geo_api():
    key = "AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=平安国际金融中心&key=%s" % (key)

    response = urllib2.urlopen(url)
    result = response.read()
    # json_text = json.loads(result)
    print ('json_text: %s' % result)
    # lng = json_text.get('geometry')
    # print ('lng: %s' % lng)


def baidu_geo_api(sight_name):
    sight_name = sight_name.decode('utf-8')
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&address=%s&ak=qsQB3G3zIR1SvZ01bEIAMBHGbCCUhTgm' % sight_name
    log.msg('run into baidu_geo_api at line 123, url: ' + url, log.INFO)
    response = urllib2.urlopen(url.encode('utf-8'))
    result = response.read()
    json_text = json.loads(result)
    if json_text.get('status') is not 1:
        lng = json_text.get('result').get('location').get('lng')
        lng = float('%.2f' % lng)
        lat = json_text.get('result').get('location').get('lat')
        lat = float('%.2f' % lat)
        return lng, lat
    else:
        log.msg('response status is 1 at line 132,' + sight_name, level=log.INFO)
        return 1, 1


def json_process():
    json_text = {"status": 0,
                 "result": {"location": {"lng": 103.40091230855559, "lat": 29.50700404085018}, "precise": 0,
                            "confidence": 14, "level": "区县"}}
    lng = json_text.get('result').get('location').get('lng')
    lng = float('%.2f' % lng)
    lat = json_text.get('result').get('location').get('lat')
    lat = float('%.2f' % lat)

    print lng
    print lat


if __name__ == '__main__':
    baidu_geo_api('周大福中心')
