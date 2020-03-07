# -*- coding: utf-8 -*-
import scrapy
from ..userdata import user


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['chaoxing.com']
    # start_urls = [user.url]

    def start_requests(self):
        url = user.url
        cookies = user.cookies
        yield scrapy.Request(url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        title = response.css('head>title').extract_first()
        print('------------------------------')
        print(title)
        print('------------------------------')
