# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# ID,date,week,max_temperature,min_temperature,weather_condition,wind_scale,year,day
class WeatherWeekItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = scrapy.Field()
    date = scrapy.Field()
    max_temperature = scrapy.Field()
    min_temperature = scrapy.Field()
    weather_condition = scrapy.Field()
    wind_scale = scrapy.Field()
    year = scrapy.Field()
    day = scrapy.Field()
    pass


