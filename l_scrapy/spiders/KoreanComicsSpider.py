# -*- coding: utf-8 -*-
import scrapy
from l_scrapy.items import KoreancomicsItem,KoreancomicsItemHua,KoreancomicsSeries,KoreancomicsSeries_Page_Url
from scrapy.loader import ItemLoader
#**********漫画名************第几话******************第几页***********************第几张***************************
fileinfo={"comics_name":"","comics_series_name":"","comics_series_page_name":"","comics_series_page_index_name":""}
class KoreancomicsspiderSpider(scrapy.Spider):
    name = 'KoreanComicsSpider'
    allowed_domains = ['vaga.cc']
    start_urls = ['http://vaga.cc/cpage_1.html'
                  ,'http://vaga.cc/cpage_2.html'
                  ,'http://vaga.cc/cpage_3.html'
                  ,'http://vaga.cc/cpage_4.html'
                  ,'http://vaga.cc/cpage_5.html'
                  ,'http://vaga.cc/cpage_6.html'
                  ,'http://vaga.cc/cpage_7.html']
    comicses=[]#所有漫画列表
    comicses_urls=[]#所有漫画列表url
    obtain_comicses_end=False
    comicsesDic={}#key 漫画名 value KoreancomicsItemHua
    def parse(self, response):
        """爬所有漫画列表"""
        for li in response.xpath("//li[@class='i_list list_n1']"):
            #print(li)
            loader=ItemLoader(KoreancomicsItem(),li)
            loader.add_xpath("title", "a[1]//img[1]/@alt[1]")
            loader.add_xpath("url", "a[1]/@href[1]")
            item=loader.load_item()
            self.comicses.append(item)
            #print("item**:",repr(item))
            pass
        #print("response.url：",response.url)
        for i in self.comicses:
            yield scrapy.Request(i["url"],meta={"comics_name":i["title"],"comics_index":i["url"]},callback=self.parse_item_comics)
        pass
    #----------------------------------------------------------------------
    def parse_item_comics(self,response):
        """爬单个漫画 只需获取第一话 之后可通过‘下一页获取‘"""
        series_urls=[]
        comics_name=""
        metaTemp=response.meta
        if("comics_name" in metaTemp):
            comics_name=metaTemp["comics_name"]
        index_url=""
        #print("解析漫画：",comics_name)
        if("comics_index" in metaTemp):
            index_url=metaTemp["comics_index"]
        #解析话数
        if(comics_name not in self.comicsesDic):
            self.comicsesDic[comics_name]=[]
            pass
        for li in response.xpath("//li[@class='i_list list_n1']"):
            loader=ItemLoader(KoreancomicsItemHua(),li)
            loader.add_xpath("title", "a[1]//img[1]/@alt[1]")
            loader.add_xpath("seriesUrl", "a[1]/@href[1]")
            item=loader.load_item()
            self.comicsesDic[comics_name].append(item)
            seriesUrl=item["seriesUrl"]
            metaTemp["comics_series_index"]=seriesUrl
            metaTemp["page"]="第1页"
            metaTemp["comics_series_name"]=item["title"]#名称：第几话
            yield scrapy.Request(seriesUrl,callback=self.parse_comics_series_image,meta=metaTemp)
            break#获得第一话首地址（也是该话第一页 之后可通过下一页获取）即可
            
        #print("self.comicsesDic:",self.comicsesDic)
    #----------------------------------------------------------------------
    def parse_comics_series_image(self,response):
        """解析某一漫画特定话下面的所有图片 信息里面可能会有多页数据"""
        #解析图片
        file_path=""
        suf=".jpg"
        metaTemp=response.meta
        comics_series_name=""
        #获取漫画 话数
     
        for title in response.xpath("//div[@class='item_title']//h1[1]//text()"):#??????????????span
         
            comics_series_name=title.extract()
            print("话数：",comics_series_name)
            break
            
        for div in response.xpath("//div[@class='image_div']"):#获取某一页下面的所有图片
            loader=ItemLoader(KoreancomicsSeries(),div)
            loader.add_xpath("image_urls", "p//a[1]//img[1]/@src")
            loader.add_value("comics_name",metaTemp["comics_name"])
            loader.add_value("comics_series_name",comics_series_name)
            #loader.add_value("page",metaTemp["page"])
            item=loader.load_item()  
            print(item)
            yield item
           
            pass
        
        #for a_tag in response.xpath("//img//@src"):
            #item=KoreancomicsSeries()
            #item["imageurls"].append(a_tag.extract())
        
        #获取所有页信息
        urls=[]
        index_url=""
        for next_page in response.xpath("//a[@class='page-numbers prev']//@href"):
            next_page_url=next_page.extract()
            print("下一页",next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse_comics_series_image,meta=metaTemp)
            break
                   
       
    ##----------------------------------------------------------------------
    #def parse_item_comics(self,response):
        #"""爬单个漫画 解析所有话    可能包括多页"""
        #series_urls=[]
        #comics_name=""
        #metaTemp=response.meta
        #if("comics_name" in metaTemp):
            #comics_name=metaTemp["comics_name"]
        #index_url=""
        ##print("解析漫画：",comics_name)
        #if("comics_index" in metaTemp):
            #index_url=metaTemp["comics_index"]
        ##解析话数
        #if(comics_name not in self.comicsesDic):
            #self.comicsesDic[comics_name]=[]
            #pass
        #for li in response.xpath("//li[@class='i_list list_n1']"):
            #loader=ItemLoader(KoreancomicsItemHua(),li)
            #loader.add_xpath("title", "a[1]//img[1]/@alt[1]")
            #loader.add_xpath("seriesUrl", "a[1]/@href[1]")
            #item=loader.load_item()
            #self.comicsesDic[comics_name].append(item)
            #seriesUrl=item["seriesUrl"]
            #metaTemp["comics_series_index"]=seriesUrl
            #metaTemp["page"]="第1页"
            #metaTemp["comics_series_name"]=item["title"]#名称：第几话
            #yield scrapy.Request(seriesUrl,callback=self.parse_comics_series_image,meta=metaTemp)
            #pass
        ##print("self.comicsesDic:",self.comicsesDic)
        #urls=[]
        #if(index_url==response.url):#如果是首页则解析其他页面url所含的话数 
            #for tag_a in response.xpath("//a[@class='page-numbers']//@href"):#截取某部动画所有页数url
                #url=tag_a.extract()
                #urls.append(url)
                #yield scrapy.Request(url,callback=self.parse_item_comics,meta=metaTemp)
                #pass
            ##print("parse_i            tem_comics**:",urls)
            
            #pass
    ##----------------------------------------------------------------------
    #def parse_comics_series_image(self,response):
        #"""解析某一漫画特定话下面的所有图片 信息里面可能会有多页数据"""
        ##解析图片
        #file_path=""
        #suf=".jpg"
        #metaTemp=response.meta
        ##获取漫画 话数
        #for title in response.xpath("//div[@class='item_title/h1[1]/text()']"):
            #comics_series_name=title.extract()
            #pass
        #for div in response.xpath("//div[@class='image_div']"):#获取某一页下面的所有图片
            #loader=ItemLoader(KoreancomicsSeries(),div)
            #loader.add_xpath("image_urls", "p//a[1]//img[1]/@src")
            #loader.add_value("comics_name",metaTemp["comics_name"])
            #loader.add_value("comics_series_name",metaTemp["comics_series_name"])
            #loader.add_value("page",metaTemp["page"])
            #item=loader.load_item()  
            ##print(item)
            #yield item
           
            #pass
        
        ##for a_tag in response.xpath("//img//@src"):
            ##item=KoreancomicsSeries()
            ##item["imageurls"].append(a_tag.extract())
        
        ##获取所有页信息
        #urls=[]
        #index_url=""
        #if("comics_series_index" in response.meta):
            #index_url=response.meta["comics_series_index"]
        #if(index_url==response.url):#如果是首页则解析其他页面url 
            #for tag_a in response.xpath("//a[@class='page-numbers']"):#截取某部动画所有页数url
                #loader_page=ItemLoader(KoreancomicsSeries_Page_Url(),tag_a)
                #loader_page.add_xpath("page","@title")
                #loader_page.add_xpath("url","@href")
               
                #item=loader_page.load_item()
                #metaTemp["page"]=item["page"].replace(" ","")
                #url=item["url"]
                #urls.append(url)
                #yield scrapy.Request(url,callback=self.parse_comics_series_image,meta=metaTemp)
                #pass
       
       
       
        
        
