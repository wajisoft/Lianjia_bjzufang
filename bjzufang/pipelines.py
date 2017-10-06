# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BjzufangPipeline(object):
    def __init__(self):
        self.filename = open('lianjia.json', 'a')

    def process_item(self, item, spider):
        # fieldname = ['name','zone','area','orientation','district','floor','time','money','see_num','latitude','city']
        # writer = csv.DictWriter(self.filename,fieldnames=fieldname)
        # writer.writeheader()
        # writer.writerow(item)
        line = json.dumps(dict(item)) + '\n'
        self.filename.write(line)
        return item
