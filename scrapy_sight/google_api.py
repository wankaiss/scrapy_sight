# -*- coding: utf-8 -*-
import requests


def google_geo_api():
    key = "申请自己的api"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=东方明珠&key=AIzaSyAw-IJpHf6CYtb4OVgrj2MB7pmXlbSs7aY%s" % key
    print ('test==================: %s' % url)
    # response = urllib2.urlopen(url)
    # result = response.read()
    session = requests.Session()
    session.proxies = {"http": "http://127.0.0.1:1080"}
    req = session.get(url)
    json = req.json()
    print ('json_text: %s' % json)


google_geo_api()
