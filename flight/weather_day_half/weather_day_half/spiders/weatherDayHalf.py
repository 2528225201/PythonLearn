# -*- coding: utf-8 -*-
import sys

import scrapy
print (sys.path)
from weather_day_half.items import WeatherDayHalfItem


class WeatherdayhalfSpider(scrapy.Spider):
    name = 'weatherDayHalf'
    allowed_domains = ['heweather.com']
    start_urls = ['https://www.heweather.com/severe-weather/beijing-101010100.html',
                  'https://www.heweather.com/severe-weather/shanghai-101020100.html',
                  'https://www.heweather.com/severe-weather/xian-101110101.html',
                  'https://www.heweather.com/severe-weather/chengdu-101270101.html']

    def parse(self, response):
        # 城市
        city = response.xpath('//div[@class="weather-sub-menu"]//div//h1//text()').get()
        # 气象灾害预警
        try:
            # level = response.xpath('//div[@class="t"]//div//div[@class="sk_alarm"]//a//@class').get()
            # disaster = response.xpath('//div[@class="t"]//div//div[@class="sk_alarm"]//a//text()').get()
            warning = response.xpath('/html/body/div[5]/section[1]/div/div/div[1]/div[1]/div/div[1]/h1//text()').get()
            warning = warning[warning.rfind('布') + 1:]
        except AttributeError as e:
            warning = '无'

        item = WeatherDayHalfItem()

        if (city == "北京"):
            city = "bj"
        if (city == "上海"):
            city = "sh"
        if (city == "西安"):
            city = "xa"
        if (city == "成都"):
            city = "cd"

        item['city'] = city
        # item['precipitation'] = precipitation
        item['warning'] = warning
        yield item
