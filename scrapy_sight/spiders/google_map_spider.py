# -*- coding: utf-8 -*-

import scrapy
# 附近查找
#   景点
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=31.2396889,121.4997553&radius=50000&type=TouristAttraction&keyword=景点&key=
#   购物
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=31.2396889,121.4997553&radius=50000&type=shoppingCenter&keyword=shopping&key=
#   餐厅
# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?language=zh_CN&location=31.2396889,121.4997553&radius=50000&type=restaurant&keyword=food&key=
# 下一页查找
# https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=CpQCAgEAAFxg8o-eU7_uKn7Yqjana-HQIx1hr5BrT4zBaEko29ANsXtp9mrqN0yrKWhf-y2PUpHRLQb1GT-mtxNcXou8TwkXhi1Jbk-ReY7oulyuvKSQrw1lgJElggGlo0d6indiH1U-tDwquw4tU_UXoQ_sj8OBo8XBUuWjuuFShqmLMP-0W59Vr6CaXdLrF8M3wFR4dUUhSf5UC4QCLaOMVP92lyh0OdtF_m_9Dt7lz-Wniod9zDrHeDsz_by570K3jL1VuDKTl_U1cJ0mzz_zDHGfOUf7VU1kVIs1WnM9SGvnm8YZURLTtMLMWx8-doGUE56Af_VfKjGDYW361OOIj9GmkyCFtaoCmTMIr5kgyeUSnB-IEhDlzujVrV6O9Mt7N4DagR6RGhT3g1viYLS4kO5YindU6dm3GIof1Q&key=
# 地点详情
# https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJDTwzJEGuEmsRw4ifQGYDkww&key=
# 根据photo-reference查找图片
# https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAApJSns__-0__gPovihJDzG2KFvxMEn11cfihtG8CxrAN774ZEtkJ3upySaqKy6RrPWWY3WIXwF6WBz5TII3g9Zs_XoIV_A0vzwMMyJPRlR18aL46GR4m7mbeOCvI3Jn8kEhBE6b0Lk2I0ocXawDSaP3nsGhQWpiYbcGvmwKL04tcYRD-7kBmX5w&key=
# google geocoding
# https://maps.googleapis.com/maps/api/geocode/json?address=金茂大厦&key=