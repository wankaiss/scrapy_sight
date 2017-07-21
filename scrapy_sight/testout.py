# -*- coding: utf-8 -*-
import json

str_text = """
{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "1",
               "short_name" : "1",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Rådhusplassen",
               "short_name" : "Rådhusplassen",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Sentrum",
               "short_name" : "Sentrum",
               "types" : [ "political", "sublocality", "sublocality_level_1" ]
            },
            {
               "long_name" : "Oslo",
               "short_name" : "Oslo",
               "types" : [ "postal_town" ]
            },
            {
               "long_name" : "Oslo kommune",
               "short_name" : "Oslo kommune",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Oslo",
               "short_name" : "Oslo",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "Norway",
               "short_name" : "NO",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "0037",
               "short_name" : "0037",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "Rådhusplassen 1, 0037 Oslo, Norway",
         "geometry" : {
            "location" : {
               "lat" : 59.9121487,
               "lng" : 10.7337252
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 59.9134976802915,
                  "lng" : 10.7350741802915
               },
               "southwest" : {
                  "lat" : 59.91079971970849,
                  "lng" : 10.7323762197085
               }
            }
         },
         "place_id" : "ChIJpaMsOYduQUYRvIhIclNW9lI",
         "types" : [
            "city_hall",
            "establishment",
            "local_government_office",
            "point_of_interest"
         ]
      }
   ],
   "status" : "OK"
}
"""

json_loads = json.loads(str_text)
location = json_loads.get('results')[0].get('geometry').get('location')
lat = location.get('lat')
lat = float('%.2f' % lat)
lng = location.get('lng')
lng = float('%.2f' % lng)
print 'lat: %s\r\n lng: %s' % (float('%.2f' % lat), float('%.2f' % lng))
