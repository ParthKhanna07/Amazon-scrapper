# -*- coding: utf-8 -*-
import scrapy

from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/s?k=books&i=digital-text&ref=nb_sb_noss_2']

    def parse(self, response):
        items = AmazonItem()
        name = response.css('.a-color-base.a-text-normal::text').extract()
        author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        price = response.css('.a-price-whole').css('::text').extract()
        items['name']=name
        items['author']=author
        items['price']=price
        yield items
        
