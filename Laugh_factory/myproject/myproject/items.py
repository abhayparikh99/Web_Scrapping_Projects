# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    joke = scrapy.Field()
    likes = scrapy.Field()
    dislikes = scrapy.Field()
    
