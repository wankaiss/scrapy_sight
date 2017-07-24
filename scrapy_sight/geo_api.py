# -*- coding: utf-8 -*-
import urllib2
import json
from scrapy import log


def google_geo_api(sight_name):
    sight_name = sight_name.decode('utf-8')
    key = "AIzaSyDJtV9r7rAr9EBwlQ8Rbxvo6e7CkJsLn4k"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (sight_name, key)
    print 'url: %s' % url
    response = urllib2.urlopen(url.encode('utf-8'))
    result = response.read()
    json_loads = json.loads(result)
    if json_loads.get('status') == 'OK':
        location = json_loads.get('results')[0].get('geometry').get('location')
        lat = location.get('lat')
        lat = float('%.2f' % lat)
        lng = location.get('lng')
        lng = float('%.2f' % lng)
        print ('lat: %s\r\n lng %s' % (lat, lng))
        return lng, lat
    else:
        log.msg('There is no result about lat and lng')
        return 1, 1
        # json_text = json.loads(result)
        # lng = json_text.get('geometry')
        # print ('lng: %s' % lng)


def baidu_geo_api(sight_name):
    sight_name = sight_name.decode('utf-8')
    ak = 'qsQB3G3zIR1SvZ01bEIAMBHGbCCUhTgm'
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&address=%s&ak=%s' % (sight_name, ak)
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
    google_geo_api('上海中心大厦')
    # lng, lat = baidu_geo_api('上海中心大厦')
    # print lng, '\r\n', lat
