# -*- coding: utf-8 -*-

import scrapy
import logging
from scrapy.http import Request
from scrapy.selector import Selector
from fundbot.items import FundbotItem
import re
import json

class Spider(scrapy.Spider):
    name = 'fundbot'
    host = 'https://www.howbuy.com/'
    filterPage = 'fund/ajax/fundtool/newfilter.htm'
    ajax_bodys = ['fundTypeCode=3&yjpmCode=4-1&yjpmCode=5-1&jjgmCode=20-100&yjpmCode=6-1', # 混合型，近1、2、3年前1/4，规模20-100亿
                  'fundTypeCode=8&fzfsCode=511&gzzsCode=0&zsnhdCode=1', # 大盘指数，完全复制型，指数拟合度前1/4
                  'fundTypeCode=8&fzfsCode=511&zsnhdCode=1&gzzsCode=2'] # 小盘指数，完全复制性，指数拟合度前1/4

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.basicConfig(level = logging.DEBUG,
                        format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt = '%a, %d %b %Y %H:%M:%S',
                        filename = 'cataline.log',
                        filemode = 'w')
    @staticmethod
    def formatPercent(inputStr):
        return float(inputStr[:-1]) if inputStr is not None else float(0)

    def start_requests(self):
        for index, body in enumerate(self.ajax_bodys):
            request = Request(url = self.host + self.filterPage,
                          method = 'post',
                          body = body,
                          callback = self.parse)
            request.meta['current_page'] = 1
            request.meta['body_index'] = index
            yield request

    def parse(self, response):
        selector = Selector(response)
        trs = selector.xpath('//tbody/tr')
        pages = int(json.loads(selector.xpath('//label[@id="viewJson"]/text()').extract_first())['page']['viewPage'])
        current_page = response.meta['current_page']
        body_index = response.meta['body_index']
        current_body = self.ajax_bodys[body_index]

        fund_type_suffix = ''
        if body_index == 1:
            fund_type_suffix = u'大盘型'
        elif body_index == 2:
            fund_type_suffix = u'小盘型'
        else:
            pass
        logging.debug('fund_type_suffix_____________>' + fund_type_suffix)
        for tr in trs:
            item = FundbotItem()

            detail_path = tr.xpath('td[contains(@class, "tdl n nname")]/a/@href').extract_first()[1:]

            item['name'] = tr.xpath('td[1]/input/@jjjc').extract_first()
            item['code'] = tr.xpath('td[1]/input/@jjdm').extract_first()
            item['ftype'] = tr.xpath('td[3]/text()').extract_first() + fund_type_suffix
            item['unit_price'] = float(tr.xpath('td[4]/text()').extract_first().strip())
            item['last_1month'] = self.formatPercent(tr.xpath('td[7]/span/text()').extract_first())
            item['last_3month'] = self.formatPercent(tr.xpath('td[8]/span/text()').extract_first())
            item['last_6month'] = self.formatPercent(tr.xpath('td[9]/span/text()').extract_first())
            item['last_1year'] = self.formatPercent(tr.xpath('td[10]/span/text()').extract_first())
            item['last_2year'] = self.formatPercent(tr.xpath('td[11]/span/text()').extract_first())
            item['last_3year'] = self.formatPercent(tr.xpath('td[12]/span/text()').extract_first())

            request = Request(url = self.host + detail_path,
                          callback=self.parse_fund)
            request.meta['item'] = item
            yield request

        if current_page < pages:
            request = Request(url = self.host + self.filterPage,
                        method = 'post',
                        body = current_body + '&page=' + str(current_page + 1),
                        callback = self.parse)
            logging.debug('current page-------------->' + current_body + '&page=' + str(current_page + 1))
            request.meta['body_index'] = body_index
            request.meta['current_page'] = current_page + 1
            yield request

    def parse_fund(self, response):
        item = response.meta['item']
        selector = Selector(response)
        item['size'] = float(selector.xpath('//div[@class="gmfund_num"]/ul/li[3]/span/text()').extract_first()[:-1])
        item['fund_create_time'] = selector.xpath('//div[@class="gmfund_num"]/ul/li[4]/span/text()').extract_first()
        item['manager_name'] = selector.xpath('//div[@class="manager_b_r"]/div[@class="info"]/ul[1]/li[1]/a/text()').extract_first()
        item['manage_fund_number'] = int(selector.xpath('//div[@class="manager_b_r"]/div[@class="info"]/ul[2]/li[2]/a/text()').extract_first()[:-1])
        item['manage_time'] = selector.xpath('//span[@class="businessH"]/text()').extract_first()[5:]
        item['fund_comp_name'] = selector.xpath('//div[@class="file_Co"]//li[contains(text(), ' + u'公司简介' + ')]/a/text()').extract_first()
        yield item
