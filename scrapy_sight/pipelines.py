# -*- coding: utf-8 -*-
from pyArango.connection import *


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class SightPipeline(object):
    def __init__(self):
        self.conn = Connection(username='ybbapp', password='se4dr5ft6', arangoURL='http://172.26.30.57:8529')
        self.db = self.conn['ybbapp']

    def process_item(self, item, spider):
        scrapy_data = self.db['scrapy_data']
        doc = scrapy_data.createDocument()
        doc['result'] = item
        doc.save()
        try:
            if item['google_message'] is not None and len(item['google_message']) != 0:
                google_message = self.db['google_message']
                doc_google = google_message.createDocument()
                doc_google['result'] = item['google_message']
                doc_google.save()
        except KeyError as e:
            print e
