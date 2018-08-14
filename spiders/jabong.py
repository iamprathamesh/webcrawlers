# -*- coding: utf-8 -*-
import scrapy
from flask import Request


class JabongSpider(scrapy.Spider):
    name = 'jabong'
    allowed_domains = ['https://www.jabong.com']
    url = 'https://www.jabong.com/find/{}/?q={}&tt={}&rank=0&qc={}'
    start_urls = [url.format('nike')]

    def parse(self, response):



        # price = price[0] if price else ''

        item = {
            'url':response.url,
            'brand':brand,
            'price':price
        }
        yield item