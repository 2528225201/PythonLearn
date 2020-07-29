# -*- coding: utf-8 -*-
import datetime

import scrapy

from weather_week.items import WeatherWeekItem


class WeatherweekSpider(scrapy.Spider):
    name = 'weatherWeek'
    allowed_domains = ['weather.com.cn']
    start_urls = ['http://www.weather.com.cn/weather/101010100.shtml',   #北京
                  'http://www.weather.com.cn/weather/101020100.shtml',   #上海
                  'http://www.weather.com.cn/weather/101110101.shtml',   #西安
                  'http://www.weather.com.cn/weather/101270101.shtml']   #成都
    citys = ['北京', '上海', '西安', '成都']

    def parse(self,response):
        city = self.citys.pop(0)
        # 提取对应数据所在标签
        selectors = response.xpath('//div[@class="left fl"]//div[1]//div[@id="7d"]//ul//li')
        # 循环遍历li标签
        # ID,date,week,max_temperature,min_temperature,weather_condition,wind_scale,year,day
        for selector in selectors:
            # 天气编号   0
            ID = ''.join([str(i) for i in city])
            # 日期   1
            date = selector.xpath('.//h1//text()').get()
            # 最高温度      1
            max_temperature = selector.xpath('.//p[@class="tem"]//span//text()').get()
            # 最低温度      1
            min_temperature = selector.xpath('.//p[@class="tem"]//i//text()').get()
            # 天气情况   1
            weather_condition = selector.xpath('.//p[@class="wea"]//text()').get()
            # 风力等级      1
            wind_scale = selector.xpath('.//p[@class="win"]//i//text()').get()
            # 年     1
            year = datetime.datetime.now().strftime('%Y')
            # 天数    一年中第几天      1
            day = datetime.datetime.now().strftime('%j')
            # # 若出发日期未选定，选择当天  数据格式：2020-01-01
            # if flight_date == '':
            #     flight_date = datetime.datetime.now().strftime('%Y-%m-%d')

            print(ID,date,max_temperature,min_temperature,weather_condition,wind_scale,year,day)

            item = WeatherWeekItem()
            #设置唯一主键为城市+日期
            item['ID'] = ID+date
            item['date'] = date
            item['max_temperature'] = max_temperature
            item['min_temperature'] = min_temperature
            item['weather_condition'] = weather_condition
            item['wind_scale'] = wind_scale
            item['year'] = year
            item['day'] = day
            print(item)
            yield item
