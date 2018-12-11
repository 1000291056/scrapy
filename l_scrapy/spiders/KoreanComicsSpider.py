# -*- coding: utf-8 -*-
import scrapy
from l_scrapy.items import KoreancomicsItem
from scrapy.loader import ItemLoader

class KoreancomicsspiderSpider(scrapy.Spider):
    name = 'KoreanComicsSpider'
    allowed_domains = ['vaga.cc']
    start_urls = ['http://vaga.cc/']

    def parse(self, response):
        """爬所有漫画列表"""
        #filePath="bg.html"
        #file= open(filePath,"w",encoding="utf-8")
        #file.write(response.text)
        #每个页面的图片列表为<li class=i_list list_n1>
        items=[]
        for li in response.xpath("//li[@class='i_list list_n1']"):
            #print(li)
            #loader=ItemLoader(KoreancomicsItem(),li)
            #loader.add_xpath("title", "//a[0]//img[0]/@alt")
            #loader.add_xpath("url", "//a[0]/@href")
            #item=loader.load_item
            #items.append(item)
           
            item=KoreancomicsItem()
            item["title"]=li.xpath("a[1]//img[1]/@alt").extract()[0]
            item["url"]=li.xpath("a[1]//@href").extract()[0]
            items.append(item)
            print("item**:",repr(item))
            pass
        filePath="bg.json"
        file= open(filePath,"w",encoding="utf-8")
        file.write(repr(items))        
        
        pass
    #----------------------------------------------------------------------
    def parse_item_comics(self,response):
        """爬单个漫画"""
        
