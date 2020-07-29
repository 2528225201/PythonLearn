# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherDayMinuteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = scrapy.Field()
    city = scrapy.Field()
    weather = scrapy.Field()
    temperature = scrapy.Field()
    visibility = scrapy.Field()
    pressure = scrapy.Field()
    air_density_now = scrapy.Field()
    warning = scrapy.Field()
    pass
