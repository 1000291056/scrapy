# -*- coding: utf-8 -*-
import scrapy
from l_scrapy.items import ItcastItem
from scrapy.loader import ItemLoader
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
    custom_settings={"some_setting":"some_value"}

    def parse(self, response):
        filename="teacher.html"
        #print("Existing settings: %s" % self.settings.attributes.keys())
    
        #open(filename,"w",encoding="utf-8").write(response.text)
       # 存放老师信息的集合
        items = []
        print("****************************")
        for each in response.xpath("body//div[@class='li_txt']"):
            print(each)
        #for each in response.xpath("//div[@class='li_txt']"):
            ## 将我们得到的数据封装到一个 `ItcastItem` 对象
            #item = ItcastItem()
            ##extract()方法返回的都是unicode字符串
            #name = each.xpath("h3/text()").extract()
            #title = each.xpath("h4/text()").extract()
            #info = each.xpath("p/text()").extract()
            ##xpath返回的是包含一个元素的列表
            #item['name'] = name[0]
            #item['title'] = title[0]
            #item['info'] = info[0]

            #items.append(item)
        for each in response.xpath("//div[@class='li_txt']"):
            l=ItemLoader(ItcastItem(),each)
            l.add_xpath("name","h3[1]/text()")
            l.add_xpath("title","h4[1]/text()")
            l.add_xpath("info","p[1]/text()")
            l.add_value("time","today")
            items.append(l.load_item())
        return items       
        
