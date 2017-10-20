# coding: gbk
from pyArango.connection import *


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class SightPipeline(object):
    def __init__(self):
        self.conn = Connection(username='root', password='se4dr5ft6', arangoURL='http://172.26'
                                                                                '.30.92:8529')
        self.db = self.conn['ybbapp']

    def process_item(self, item, spider):
        scrapy_data = self.db['ctrip_data']
        doc = scrapy_data.createDocument()
        doc['result'] = item
        doc.save()
