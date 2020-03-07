# -*- coding: utf-8 -*-
import scrapy
from ..items import ChaoxingItem
from ..userdata import user
import re


class KejianSpider(scrapy.Spider):
    name = 'kejian'
    allowed_domains = ['chaoxing.com']
    # start_urls = ['http://chaoxing.com/']

    def start_requests(self):
        yield scrapy.Request(url=user.url, cookies=user.cookies, callback=self.parse_article_url)

    def parse_article_url(self, response):
        urls = response.css('span.articlename>a::attr(href)').extract()
        for url in urls:
            data = {i.split('=')[0]: i.split('=')[1] for i in url.split('?')[1].split('&')}
            m_url = 'https://mooc1-1.chaoxing.com/knowledge/cards?clazzid={}&courseid={}&knowledgeid={}'.format(data['clazzid'], data['courseId'], data['chapterId'])
            yield scrapy.Request(url=m_url, cookies=user.cookies, callback=self.parse_file_url)

    def parse_file_url(self, response):
        id = re.findall('"objectid":"(.*?)"', response.text)[0]
        f_url = f'http://d0.ananas.chaoxing.com/download/{id}'
        yield scrapy.Request(url=f_url, cookies=user.cookies, callback=self.parse)

    def parse(self, response):
        item = ChaoxingItem()
        item['name'] = re.findall('filename=(.*?);filename\\*', response.headers['Content-Disposition'].decode('utf-8'))[0]
        item['file_urls'] = [response.request.url]
        yield item
