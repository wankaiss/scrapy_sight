# -*- coding: utf-8 -*-
import urllib2
import json


def google_geo_api():
    address = "1600+Amphitheatre+Parkway,+Mountain+View,+CA"
    key = "请自行申请"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, key)

    response = urllib2.urlopen(url)
    jsongeocode = response.read()
    print jsongeocode


def baidu_geo_api(sight_name):
    url = 'http://api.map.baidu.com/geocoder/v2/?output=json&address=%s&ak=请自行申请' % sight_name
    response = urllib2.urlopen(url)
    result = response.read()
    json_text = json.loads(result)

    lng = json_text.get('result').get('location').get('lng')
    lng = float('%.2f' % lng)
    lat = json_text.get('result').get('location').get('lat')
    lat = float('%.2f' % lat)

    return lng, lat


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
    lng, lat = baidu_geo_api('峨眉山')
    print lng
    print lat
