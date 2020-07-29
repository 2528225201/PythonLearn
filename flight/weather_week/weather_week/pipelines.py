# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
from pymysql import IntegrityError

class WeatherWeekPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='toor', db='flight', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 往数据库里面写入数据
            self.cursor.execute(
                'insert into weather_week(ID,date,max_temperature,min_temperature,weather_condition,wind_scale,year,day) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                    item['ID'], item['date'],  item['max_temperature'], item['min_temperature'],
                    item['weather_condition'], item['wind_scale'], item['year'], item['day']))
            self.connect.commit()
            return item
        except IntegrityError as e:
            print("重复数据，跳过")


    #关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
