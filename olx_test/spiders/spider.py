# -*- coding: utf-8 -*-
import scrapy
import json

from olx_test.items import OlxTestItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    # allowed_domains = ['www.olx.co.id']
    start_urls = ['https://www.olx.co.id/mobil-bekas_c198']

    PAGE_URL = 'https://www.olx.co.id/api/relevance/search?category=198&facet_limit=100&location=1000001&' \
               'location_facet_limit=20&page={}&user=16eeeccbdacx3537a77c'

    MAX_PAGE = 50

    def parse(self, response):
        item = OlxTestItem()
        blocks = response.xpath('//div[@class="IKo3_"]')
        # get items
        for block in blocks:
            item['price'] = block.xpath('span[@class="_89yzn"]/text()').get()
            item['name'] = block.xpath('span[@class="_2tW1I"]/text()').get()
            yield item

        # pagination
        page = 1
        while page != self.MAX_PAGE:
            url = self.PAGE_URL.format(page)
            yield scrapy.Request(url, callback=self.parse_pagination)
            page += 1

    def parse_pagination(self, response):
        # another pages pagination
        result = json.loads(response.body)['data']
        item = OlxTestItem()
        for elem in result:
            item['name'] = elem['title']
            item['price'] = elem['price']['value']['display']
            yield item
