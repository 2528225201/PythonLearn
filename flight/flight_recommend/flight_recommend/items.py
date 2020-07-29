# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlightRecommendItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = scrapy.Field()
    flight_no = scrapy.Field()
    flight_stime = scrapy.Field()
    flight_etime = scrapy.Field()
    flight_sairport = scrapy.Field()
    flight_eairport = scrapy.Field()
    flight_punrate = scrapy.Field()
    flight_date = scrapy.Field()
    pass
