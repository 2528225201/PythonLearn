# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import datetime


import scrapy

from flight_recommend.items import FlightRecommendItem


class FlightSpider(scrapy.Spider):
    name = 'flight'
    allowed_domains = ['flights.ctrip.com']
    start_urls = ['https://flights.ctrip.com/domestic/schedule/bjs.sha.html',   #北京到上海
                  'https://flights.ctrip.com/domestic/schedule/sha.bjs.html',   #上海到北京
                  'https://flights.ctrip.com/domestic/schedule/bjs.sia.html',   #北京到西安
                  'https://flights.ctrip.com/domestic/schedule/sia.bjs.html',   #西安到北京
                  'https://flights.ctrip.com/domestic/schedule/bjs.ctu.html',   #北京到成都
                  'https://flights.ctrip.com/domestic/schedule/ctu.bjs.html',   #成都到北京
                  'https://flights.ctrip.com/domestic/schedule/sha.ctu.html',   #上海到成都
                  'https://flights.ctrip.com/domestic/schedule/ctu.sha.html',   #成都到上海
                  'https://flights.ctrip.com/domestic/schedule/sha.sia.html',   #上海到西安
                  'https://flights.ctrip.com/domestic/schedule/sia.sha.html',   #西安到上海
                  'https://flights.ctrip.com/domestic/schedule/sia.ctu.html',   #西安到成都
                  'https://flights.ctrip.com/domestic/schedule/ctu.sia.html']   #成都到西安

    # 解析响应数据，提取数据或网址等,response就是下载器的响应，即网页源码
    # def parse(self, response):
    #     # 翻页操作方法2
    #     info_list = response.xpath('//li//div[3]//div[2]//div//div//div//a//@href').extract()[:3]
    #     for info in info_list:
    #         print(info)
    #         # 拼接完整的‘更多’网址
    #         yield scrapy.Request(url=info, callback=self.get_content_in_url)


    def parse(self,response):
        # 提取对应数据所在标签
        selectors = response.xpath('//li//div[3]//div[2]//table//tr')
        # 循环遍历tr标签下的td标签
        for selector in selectors:
            # 航班编号
            flight_no = selector.xpath('.//td[1]//strong//text()').get()
            if flight_no is None:  # 过略None值
                continue
            # 起飞时间
            flight_stime = selector.xpath('.//td[2]//strong//text()').get()
            # 降落时间
            flight_etime = selector.xpath('.//td[4]//strong//text()').get()
            # 起飞机场
            flight_sairport = selector.xpath('.//td[2]//div//text()').get()
            # 降落机场
            flight_eairport = selector.xpath('.//td[4]//div//text()').get()
            # 准点率
            flight_punrate = selector.xpath('.//td[6]//text()').get()
            if flight_punrate == '-':
                continue
            # 出发日期
            flight_date = str(selector.xpath('.//td[8]//input//@value').get())
            # 若出发日期未选定，选择当天  数据格式：2020-01-01
            if flight_date == '':
                flight_date = datetime.datetime.now().strftime('%Y-%m-%d')

            print(flight_no, flight_stime, flight_etime, flight_sairport, flight_eairport, flight_punrate, flight_date)

            item = FlightRecommendItem()
            #设置唯一主键为航班编号+起飞日期时间
            item['ID'] = flight_no+'-'+flight_date+'-'+flight_stime
            item['flight_no'] = flight_no
            item['flight_stime'] = flight_stime
            item['flight_etime'] = flight_etime
            item['flight_sairport'] = flight_sairport
            item['flight_eairport'] = flight_eairport
            item['flight_punrate'] = flight_punrate
            item['flight_date'] = flight_date
            print(item)
            yield item
        try:
            if response.xpath('//div[1]//a[@class="schedule_down"]//@href').extract()[0]:
                # 拼接网址
                next_url = response.xpath('//div[1]//a[@class="schedule_down"]//@href').extract()[0]
                # 发出请求   Request callback是回调函数，将请求得到的响应交给自己处理
                # Request()发送请求 类似request.get()
                # callback 是将发出去的请求得到的响应还交给自己处理
                scrapy.Request(next_url, callback=self.parse)
        except IndexError as e:
            print("数据读取完成")















