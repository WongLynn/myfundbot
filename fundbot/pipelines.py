# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from items import FundbotItem

class FundbotPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["MyFundBot"]
        self.MixFunds = db["MixFunds"]
        self.MixFunds.drop()

    def process_item(self, item, spider):
        print 'MongoDBItem', item
        if isinstance(item, FundbotItem):
            print 'FundbotItem True'
            try:
                self.MixFunds.insert(dict(item))
            except Exception:
                pass
        return item