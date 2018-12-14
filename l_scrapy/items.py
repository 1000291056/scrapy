# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class LScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    time=scrapy.Field()
    pass

class KoreancomicsItem(scrapy.Item):
    
    title = scrapy.Field(output_processor=TakeFirst())#某漫画名称
    url = scrapy.Field(output_processor=TakeFirst())#某漫画地址
    #----------------------------------------------------------------------
    def _str_(self):
        """"""
        return "漫画：%(comics)  地址：%(url)"%{"comics":self.title,"url":self.url}
        
class KoreancomicsItemHua(scrapy.Item):
    """某部漫画名称即首地址"""
    title = scrapy.Field(output_processor=TakeFirst())#某漫画第几话
    seriesUrl = scrapy.Field(output_processor=TakeFirst())#某漫画第几话首地址
    
class KoreancomicsSeries(scrapy.Item):
    """第几话"""
    comics_name=scrapy.Field(output_processor=TakeFirst())#漫画名称
    comics_series_name=scrapy.Field(output_processor=TakeFirst())#第几话
    page=scrapy.Field(output_processor=TakeFirst())#第几页
    title = scrapy.Field(output_processor=TakeFirst())#某漫画第几页
    image_urls = scrapy.Field()#某漫画第几话下面所有图片地址
class KoreancomicsSeries_Page_Url(scrapy.Item):
    page=scrapy.Field(output_processor=TakeFirst())#漫画某一话第几页
    url=scrapy.Field(output_processor=TakeFirst())#第几页的url
    
   