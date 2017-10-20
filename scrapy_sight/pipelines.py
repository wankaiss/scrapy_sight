# coding: gbk
from pyArango.connection import *


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class SightPipeline(object):
    def __init__(self):
        self.conn = Connection(username='username', password='password', arangoURL='127.0.0.1:8529')
        self.db = self.conn['ybbapp']

    def process_item(self, item, spider):
        scrapy_data = self.db['ctrip_data']
        doc = scrapy_data.createDocument()
        doc['result'] = item
        doc.save()
