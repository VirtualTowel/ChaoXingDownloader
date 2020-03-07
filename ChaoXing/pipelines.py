# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline


class ChaoxingPipeline(object):
    def process_item(self, item, spider):
        return item

class MyFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
       for file_url in item['file_urls']:
           yield scrapy.Request(url=file_url, meta={'name': item['name']})

    def file_path(self, request, response=None, info=None):
        name = request.meta['name']
        return name