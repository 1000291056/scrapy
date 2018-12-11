# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


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
    title = scrapy.Field()#某漫画名称
    url = scrapy.Field()#某漫画地址
    #----------------------------------------------------------------------
    def _str_(self):
        """"""
        return "漫画：%(comics)  地址：%(url)"%{"comics":self.title,"url":self.url}
        
class KoreancomicsItemHua(scrapy.Item):
    """<li class="i_list list_n1">
	<a href="http://vaga.cc/128268.html" target="_blank">
		<img class="waitpic" src="http://www.vaga.cc/wp-content/themes/cx-udy/images/thumb_2.png" data-original="http://vaga.cc/wp-content/uploads/cx_img/268/ia_10001-20-280x180-1.jpg" alt="第1话" width="280" height="180">
		<div class="postlist-imagenum"><span>57</span>张</div></a>
		<div class="case_info"><a class="meta-title" href="http://vaga.cc/128268.html"> 第1话 </a>
		<div class="meta-post">1天前<span class="cx_like"><i class="iconfont">&#xe631;</i>1<i class="iconfont">&#xe63b;</i>2029</span></div></div>
    </li>"""
    title = scrapy.Field()#某漫画第几话
    url = scrapy.Field()#某漫画第几话地址
    #----------------------------------------------------------------------
    def _str_(self):
        """"""
        return "漫画：%(comics)  地址：%(url)"%{"comics":self.title,"url":self.url}    
   