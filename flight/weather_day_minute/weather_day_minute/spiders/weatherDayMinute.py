# -*- coding: utf-8 -*-
import sys

import scrapy
print (sys.path)
from weather_day_minute.items import WeatherDayMinuteItem


class WeatherdayminuteSpider(scrapy.Spider):
    name = 'weatherDayMinute'
    allowed_domains = ['weather.com/zh-CN/weather/today/l/CHXX0008:1:CH']
    start_urls = ['https://weather.com/zh-CN/weather/today/l/71ca347e2948ee9490525aa5433fa91da6973ae51ea0f765fbe8e85b9f16c5df',     #北京
                  'https://weather.com/zh-CN/weather/today/l/9354d398796fe82a5c99f3bfc158c55853cd2b8de82aca855e552eb748476c39',     #上海
                  'https://weather.com/zh-CN/weather/today/l/469847d38b26dbfd9519a7467fbcc689c42cceb1bd104a74d6637ce8359a0fba',     #西安
                  'https://weather.com/zh-CN/weather/today/l/464e6967d2f00205cb7f8c59cd0a5929a033436e3f650addc3561470a746b252']     #成都

    def parse(self, response):
        # 城市
        city = response.xpath('//div[@class="today_nowcard"]//section//div[2]//header//span//div//h1//text()').get()[0:2]
        # 天气
        weather = response.xpath('//div[@class="today_nowcard"]//section//div[2]//div//div[3]//text()').get()
        # 目前温度
        temperature = response.xpath('//div[@class="today_nowcard-section today_nowcard-condition"]//div[2]//span//text()').get()
        # 能见度
        visibility = response.xpath('//div[@class="today_nowcard-sidecar component panel"]//tbody//tr[5]//td//span//text()').get()[:-3]
        # 气压
        pressure = response.xpath('//div[@class="today_nowcard-sidecar component panel"]//tbody//tr[4]//td//span//text()').get()[:-3].replace(',','')
        # 空气密度
        #空气密度=1.293（实际压力/标准物理大气压）*（273/实际绝对温度），绝对温度=摄氏度+273
        air_density_now = str(round(1.293*(float(pressure)/1013.25)*(273.0/(float(temperature)+273.0)),4))
        print(city, weather, temperature, visibility, pressure, air_density_now)

        item = WeatherDayMinuteItem()
        # 设置唯一主键为航班编号+起飞日期时间

        if (city == "北京"):
            city = "bj"
        if (city == "上海"):
            city = "sh"
        if (city == "西安"):
            city = "xa"
        if (city == "成都"):
            city = "cd"
        item['city'] = city
        item['weather'] = weather
        item['temperature'] = temperature
        item['visibility'] = visibility
        item['pressure'] = pressure
        item['air_density_now'] = air_density_now
        yield item