# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import time
from lxml import etree
from bjzufang.items import BjzufangItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']

    def start_requests(self):
        start_url = 'https://bj.lianjia.com/zufang/'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        referer = 'https://bj.lianjia.com/zufang/'
        cookies = {'zufang_huodong_show1':'1','lianjia_uuid':'c2b7bf0b-a801-48ce-a893-37ff6569d944','UM_distinctid':'15ee26318214ad-0dc09af24-541b3611-15f900-15ee263182218c','select_city':'110000','_jzqckmp':'1','_jzqx':'1.1507042445.1507282295.4.jzqsr=bj%2Elianjia%2Ecom|jzqct=/zufang/101102033177%2Ehtml.jzqsr:bj%2Elianjia%2Ecom|jzqct=/zufang/chaoyang/','all-lj':'78917a1433741fe7067e3641b5c01569','Hm_lvt_9152f8221cb6243a53c83b956842be8a':'1507270351,1507288826,1507289917,1507299909','Hm_lpvt_9152f8221cb6243a53c83b956842be8a':'1507299909','CNZZDATA1253477573':'10168409-1507034656-%7C1507295353','_smt_uid':'59d38e1a.6df2abc','CNZZDATA1254525948':'887686886-1507032193-%7C1507297956','CNZZDATA1255633284':'1199884759-1507035004-%7C1507296538','CNZZDATA1255604082':'1728111072-1507035507-%7C1507297224','_jzqa':'1.3027276537188182000.1507036699.1507289918.1507299909.16','_jzqc':'1','_jzqb':'1.1.10.1507299909.1','_qzja':'1.161052116.1507036698871.1507289917529.1507299908982.1507289917529.1507299908982.0.0.0.113.16','_qzjb':'1.1507299908981.1.0.0.0','_qzjc':'1','_qzjto':'45.6.0','_gat':'1','_gat_past':'1','_gat_global':'1','_gat_new_global':'1','_ga':'GA1.2.1473941731.1507036700','_gid':'GA1.2.1776321712.1507270353','_gat_dianpu_agent':'1','lianjia_ssid':'1e100fe6-d234-45cc-8294-fe3c5cd2ce90'}
        headers = {'User-Agent': user_agent, 'Referer': referer}
        yield scrapy.Request(url=start_url,headers=headers,cookies= cookies,callback=self.parse)

    def parse(self, response):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        referer = 'https://bj.lianjia.com/zufang/'
        cookies = {'zufang_huodong_show1': '1', 'lianjia_uuid': 'c2b7bf0b-a801-48ce-a893-37ff6569d944',
                   'UM_distinctid': '15ee26318214ad-0dc09af24-541b3611-15f900-15ee263182218c', 'select_city': '110000',
                   '_jzqckmp': '1',
                   '_jzqx': '1.1507042445.1507282295.4.jzqsr=bj%2Elianjia%2Ecom|jzqct=/zufang/101102033177%2Ehtml.jzqsr:bj%2Elianjia%2Ecom|jzqct=/zufang/chaoyang/',
                   'all-lj': '78917a1433741fe7067e3641b5c01569',
                   'Hm_lvt_9152f8221cb6243a53c83b956842be8a': '1507270351,1507288826,1507289917,1507299909',
                   'Hm_lpvt_9152f8221cb6243a53c83b956842be8a': '1507299909',
                   'CNZZDATA1253477573': '10168409-1507034656-%7C1507295353', '_smt_uid': '59d38e1a.6df2abc',
                   'CNZZDATA1254525948': '887686886-1507032193-%7C1507297956',
                   'CNZZDATA1255633284': '1199884759-1507035004-%7C1507296538',
                   'CNZZDATA1255604082': '1728111072-1507035507-%7C1507297224',
                   '_jzqa': '1.3027276537188182000.1507036699.1507289918.1507299909.16', '_jzqc': '1',
                   '_jzqb': '1.1.10.1507299909.1',
                   '_qzja': '1.161052116.1507036698871.1507289917529.1507299908982.1507289917529.1507299908982.0.0.0.113.16',
                   '_qzjb': '1.1507299908981.1.0.0.0', '_qzjc': '1', '_qzjto': '45.6.0', '_gat': '1', '_gat_past': '1',
                   '_gat_global': '1', '_gat_new_global': '1', '_ga': 'GA1.2.1473941731.1507036700',
                   '_gid': 'GA1.2.1776321712.1507270353', '_gat_dianpu_agent': '1',
                   'lianjia_ssid': '1e100fe6-d234-45cc-8294-fe3c5cd2ce90'}
        headers = {'User-Agent': user_agent, 'Referer': referer}
        area_item = response.xpath('//*[@id="filter-options"]/dl[1]/dd/div[1]/a')
        for area in area_item:
            try:
                # print(area)
                area_name = area.xpath('.//text()').extract().pop()
                area_id = area.xpath('.//@href').extract().pop().split('/')[-2]
                area_url =  'https://bj.lianjia.com/zufang/{}/'.format(area_id)
                print(area_name,area_id,area_url)
                if area_url == 'https://bj.lianjia.com/zufang/zufang/' \
                        or area_url == 'https://bj.lianjia.com/zufang/yanjiao/' \
                        or area_url == 'https://bj.lianjia.com/zufang/xianghe/':
                    pass
                else:
                    # print(area_name)
                    yield scrapy.Request(url=area_url,headers=headers,cookies=cookies,callback=self.parse_area,
                                         meta={'area_name':area_name,'area_id':area_id})
                time.sleep(2)
            except Exception:
                pass
            # break

    def parse_area(self,response):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        referer = 'https://bj.lianjia.com/zufang/'
        cookies = {'zufang_huodong_show1': '1', 'lianjia_uuid': 'c2b7bf0b-a801-48ce-a893-37ff6569d944',
                   'UM_distinctid': '15ee26318214ad-0dc09af24-541b3611-15f900-15ee263182218c', 'select_city': '110000',
                   '_jzqckmp': '1',
                   '_jzqx': '1.1507042445.1507282295.4.jzqsr=bj%2Elianjia%2Ecom|jzqct=/zufang/101102033177%2Ehtml.jzqsr:bj%2Elianjia%2Ecom|jzqct=/zufang/chaoyang/',
                   'all-lj': '78917a1433741fe7067e3641b5c01569',
                   'Hm_lvt_9152f8221cb6243a53c83b956842be8a': '1507270351,1507288826,1507289917,1507299909',
                   'Hm_lpvt_9152f8221cb6243a53c83b956842be8a': '1507299909',
                   'CNZZDATA1253477573': '10168409-1507034656-%7C1507295353', '_smt_uid': '59d38e1a.6df2abc',
                   'CNZZDATA1254525948': '887686886-1507032193-%7C1507297956',
                   'CNZZDATA1255633284': '1199884759-1507035004-%7C1507296538',
                   'CNZZDATA1255604082': '1728111072-1507035507-%7C1507297224',
                   '_jzqa': '1.3027276537188182000.1507036699.1507289918.1507299909.16', '_jzqc': '1',
                   '_jzqb': '1.1.10.1507299909.1',
                   '_qzja': '1.161052116.1507036698871.1507289917529.1507299908982.1507289917529.1507299908982.0.0.0.113.16',
                   '_qzjb': '1.1507299908981.1.0.0.0', '_qzjc': '1', '_qzjto': '45.6.0', '_gat': '1', '_gat_past': '1',
                   '_gat_global': '1', '_gat_new_global': '1', '_ga': 'GA1.2.1473941731.1507036700',
                   '_gid': 'GA1.2.1776321712.1507270353', '_gat_dianpu_agent': '1',
                   'lianjia_ssid': '1e100fe6-d234-45cc-8294-fe3c5cd2ce90'}
        headers = {'User-Agent': user_agent, 'Referer': referer}
        total = response.xpath('/html/body/div[4]/div[3]/div[2]/div[1]/h2/span/text()').extract().pop()
        total_pagenum = int(total) // 30 + 1
        print(response.meta['area_name'],'共有 {} 套房,{} 页。'.format(total,str(total_pagenum)))
        for i in range(1,total_pagenum+1):
            url = 'https://bj.lianjia.com/zufang/{}/pg{}/'.format(response.meta['area_id'],str(i))
            time.sleep(3)
            try:
                contents = requests.get(url,headers=headers,cookies=cookies)
                contents = etree.HTML(contents.content)
                house_item = contents.xpath('//*[@id="house-lst"]/li')
                for house in house_item:
                    item = BjzufangItem()
                    try:
                        item['name'] = house.xpath('.//span[@class="region"]/text()').pop()
                        item['zone'] = house.xpath('.//span[@class="zone"]/span/text()').pop()
                        item['area'] = house.xpath('.//span[@class="meters"]/text()').pop()
                        item['district'] = house.xpath('.//div[@class="con"]/a/text()').pop()
                        item['money'] = house.xpath('.//div[@class="price"]/span/text()').pop()
                        item['see_num'] = house.xpath('.//div[@class="square"]/div/span/text()').pop()
                        item['floor'] = house.xpath('//*[@id="house-lst"]/li[2]/div[2]/div[1]/div[2]/div/text()[1]').pop()
                        item['time'] = house.xpath('//*[@id="house-lst"]/li[2]/div[2]/div[1]/div[2]/div/text()[2]').pop()
                        item['orientation'] = house.xpath('//*[@id="house-lst"]/li[2]/div[2]/div[1]/div[1]/span[3]/text()').pop()
                        item['city'] = response.meta['area_name']
                        fang_url = house.xpath('//*[@id="house-lst"]/li[1]/div[1]/a/@href').pop()
                        item['latitude'] = self.get_latitude(fang_url)
                        # print(fang_url)
                        # print(item)
                        # break
                    except Exception:
                        pass
                    time.sleep(1)
                    yield item
            except Exception:
                pass

    def get_latitude(self, url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        referer = 'https://bj.lianjia.com/zufang/'
        cookies = {'zufang_huodong_show1': '1', 'lianjia_uuid': 'c2b7bf0b-a801-48ce-a893-37ff6569d944',
                   'UM_distinctid': '15ee26318214ad-0dc09af24-541b3611-15f900-15ee263182218c', 'select_city': '110000',
                   '_jzqckmp': '1',
                   '_jzqx': '1.1507042445.1507282295.4.jzqsr=bj%2Elianjia%2Ecom|jzqct=/zufang/101102033177%2Ehtml.jzqsr:bj%2Elianjia%2Ecom|jzqct=/zufang/chaoyang/',
                   'all-lj': '78917a1433741fe7067e3641b5c01569',
                   'Hm_lvt_9152f8221cb6243a53c83b956842be8a': '1507270351,1507288826,1507289917,1507299909',
                   'Hm_lpvt_9152f8221cb6243a53c83b956842be8a': '1507299909',
                   'CNZZDATA1253477573': '10168409-1507034656-%7C1507295353', '_smt_uid': '59d38e1a.6df2abc',
                   'CNZZDATA1254525948': '887686886-1507032193-%7C1507297956',
                   'CNZZDATA1255633284': '1199884759-1507035004-%7C1507296538',
                   'CNZZDATA1255604082': '1728111072-1507035507-%7C1507297224',
                   '_jzqa': '1.3027276537188182000.1507036699.1507289918.1507299909.16', '_jzqc': '1',
                   '_jzqb': '1.1.10.1507299909.1',
                   '_qzja': '1.161052116.1507036698871.1507289917529.1507299908982.1507289917529.1507299908982.0.0.0.113.16',
                   '_qzjb': '1.1507299908981.1.0.0.0', '_qzjc': '1', '_qzjto': '45.6.0', '_gat': '1', '_gat_past': '1',
                   '_gat_global': '1', '_gat_new_global': '1', '_ga': 'GA1.2.1473941731.1507036700',
                   '_gid': 'GA1.2.1776321712.1507270353', '_gat_dianpu_agent': '1',
                   'lianjia_ssid': '1e100fe6-d234-45cc-8294-fe3c5cd2ce90'}
        headers = {'User-Agent': user_agent, 'Referer': referer}
        response = requests.get(url,headers=headers,cookies=cookies)
        selector = etree.HTML(response.content)
        latitude = selector.xpath('/html/body/div[4]/script[10]/text()').pop()
        # time.sleep(5)
        regex = '''resblockPosition(.+)'''
        req = re.search(regex, latitude)
        content = req.group()[:-1]
        latitude_con = content.split(':')[1]
        return latitude_con[1:-1]
