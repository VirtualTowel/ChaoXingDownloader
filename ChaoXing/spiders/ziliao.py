# -*- coding: utf-8 -*-
import scrapy
from ..items import ChaoxingItem
from ..userdata import user


class ZiliaoSpider(scrapy.Spider):
    name = 'ziliao'
    allowed_domains = ['chaoxing.com']
    # start_urls = ['http://chaoxing.com/']

    def start_requests(self):
        yield scrapy.Request(user.url, cookies=user.cookies, callback=self.parse_data_url)

    def parse_data_url(self, response):
        url = response.css('div.navshow>ul>li:nth-child(3)>a::attr(href)').extract_first()
        self.url_data = {i.split('=')[0]: i.split('=')[1] for i in url.split('?')[1].split('&')}
        yield scrapy.Request(response.urljoin(url), cookies=user.cookies, meta={'folder': '资料'}, callback=self.parse_data_folder)

    def parse_data_folder(self, response):
        files = response.css('tbody#tableId02>tr')
        files_len = len(files)
        for file in files[:files_len-1]:
            if file.css('::attr(type)').extract_first() == 'afolder':
                f_id = file.css('::attr(id)').extract_first()
                f_url = 'https://mooc1-1.chaoxing.com/coursedata?courseId={}&dataId={}&classId={}&enc={}'.format(self.url_data['courseId'], f_id, self.url_data['classId'], self.url_data['enc'])
                f_name = file.css('i+a::attr(name)').extract_first()
                f_name = response.meta['folder']+'/'+f_name
                yield scrapy.Request(f_url, cookies=user.cookies, meta={'folder': f_name}, callback=self.parse_data_folder)
            else:
                objectid = file.css('::attr(objectid)').extract_first()
                url = 'https://cs-ans.chaoxing.com/download/{}'.format(objectid)
                name = file.css('i+a::attr(name)').extract_first()
                name = response.meta['folder']+'/'+name
                item = ChaoxingItem()
                item['file_urls'] = [url]
                item['name'] = name
                yield item

    def parse(self, response):
        pass
