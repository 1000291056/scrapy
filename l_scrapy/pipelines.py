# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import os
import scrapy
from scrapy.exceptions import DropItem
class LScrapyPipeline(object):
    def open_spider(self):
        
        
        pass
    #----------------------------------------------------------------------
    def close_spider(self):
        """"""
        pass
        
    def process_item(self, item, spider):
        return item
########################################################################
class MyImagePipe(ImagesPipeline):
    """"""
    IMAGES_STORE=""
    item=None

  
    #@classmethod
    #def from_crawler(cls, crawler):
        #settings = crawler.settings
        #return cls(settings.getbool('LOG_ENABLED'))    
    #----------------------------- -----------------------------------------
    def get_media_requests(self, item, info):
      
        for image_url in item['image_urls']:
            #print("url!!!!",image_url)
            request=scrapy.Request(image_url,meta=item)
            self.item=item
            yield request

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        #item['image_paths'] = image_paths
        return item
    #----------------------------------------------------------------------
    
    def file_path(self, request, response=None, info=None):
        """"""
        
        #settings=get_project_settings()
        item=request.meta
        print("file_path000",item)
        storepath_root=r"D:\Document\ffw\picture"
        #print("file_path1111")
        filename=os.path.split(request.url)[1]
        #print("file_path2222")
        comics_series_name=item["comics_series_name"].replace(" ","")
        filepath=os.path.join(*[storepath_root,item["comics_name"],comics_series_name,filename])
        print("file_path!!!!",filepath)
        return filepath
        
        
        
    
    