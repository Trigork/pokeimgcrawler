# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import re
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class MyFilesPipeline(FilesPipeline):
    def file_key(self, url):
        image_guid = url.split('/')[-1]
        info = re.match("(\d+)(.*)\.png", image_guid)
        return 'full/%s' % (info.group(1)+'-'+info.group(2)+'.png')


class PokeimgcrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


