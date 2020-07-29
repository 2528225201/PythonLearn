# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class WeatherDayHalfPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='toor', db='flight', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""select * from weather_day where city = %s""", item['city'])
            ret = self.cursor.fetchone()
            if ret:
                self.cursor.execute(
                    """update weather_day set warning = %s  
                        where city  = %s""",
                    (
                    item['warning'],
                    item['city'],))
            else:
                self.cursor.execute(
                    """insert into weather_day(city,warning)
                      value (%s,%s)""",
                    (item['city'], item['warning'],))
                self.connect.commit()
        except Exception as error:
            print("错误")
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
