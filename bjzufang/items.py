# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BjzufangItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 房屋结构
    zone = scrapy.Field()
    # 房屋面积
    area = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 地区
    district = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 年代
    time = scrapy.Field()
    # 房租
    money = scrapy.Field()
    # 看过人数
    see_num = scrapy.Field()
    #坐标
    latitude = scrapy.Field()
    #城市
    city = scrapy.Field()