import time
import os

while True:
    os.chdir("D:\exercise\\flight\weather_day_minute")
    os.system("scrapy crawl weatherDayMinute ")
    os.chdir("D:\exercise\\flight\weather_day_half")
    os.system("scrapy crawl weatherDayHalf ")
    time.sleep(600)  # 每隔十分钟运行一次 60*10=600s
