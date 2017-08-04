# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class FundbotItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    code = Field()
    ftype = Field()
    unit_price = Field()
    last_1month = Field()
    last_3month = Field()
    last_6month = Field()
    last_1year = Field()
    last_2year = Field()
    last_3year = Field()
    size = Field()
    fund_create_time = Field()
    manager_name = Field()
    manage_fund_number = Field()
    manage_time = Field()
    fund_comp_name = Field()