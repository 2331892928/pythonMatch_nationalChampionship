"""
任务详情
程序给定一组经纬度（lat, lon）和一组时间数据 dt，根据经纬度从 city_attributes 工作表中查找对应的城市，再根据时间和城市从 temperature 工作表中找到对应某城市在某时间的温度数据。最后，将温度数据返回到后台判定程序。

参数 lat 表示维度，lon 表示精度。
如给定精度 lat = 49.24966, lon = -123.119339, dt='2017年1月1日1时'
查询到对应的城市是 Vancouver，再根据城市和 dt 查询到对应的温度是 1.17。



任务要求
程序给定经纬度 lon 和 lat 的数据类型是 float，时间数据 dt 的数据类型是 str；

程序返回结果的数据类型是 float；

注意，Pandas 处理后的数字的数据类型是 np.float64，需要手动将其转换为 float 类型，否则可能导致判定程序判定错误。

测试用例
输入：lat = 32.783058, lon = -96.806671, dt = '2017年01月19日18时'
输出：12.2
解释：首先根据经纬度查找城市，根据表中查询可知，符合输入经纬度的城市是Dallas，再结合表的时间可知，符合条件的温度是 12.2 度

输入：lat = 42.358429, lon = -71.059769, dt = '2017年01月09日19时'
输出：-7.12

附件信息
abroad_weather.xlsx

abroad weather 工作簿可以由 Excel 直接打开。工作簿中由两个工作表，分别是 city_attributes （城市属性）工作表和 temperature （温度）工作表。

city_attributes 工作表。工作表存放城市所属国家和所在经纬度，共 36 条信息。表格共包含 37 行 4 列。

temperature 工作表。工作表存放 city_attributes 工作表中的所有城市在 2017年 1 月和 2 月的温度（摄氏度）信息，天气以小时为分割，共 1416 条数据。工作表共 1417 行 37 列。



部分词汇含义（城市名未列出）：

词汇	含义
abroad weather	国外天气
city	城市
Country	国家
Latitude	维度
Longitude	经度
United States	美国
Canada	加拿大
Israel	以色列
datetime	日期


http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/265/fj_5324_abroad_weather.xlsx

"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
import re
from datetime import datetime

import pandas as pd


class Solution:

    def weather_searching(self, lat: float, lon: float, dt: str) -> float:
        df = pd.read_excel("http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/265/fj_5324_abroad_weather.xlsx",
                           sheet_name=None)
        city_df = df['city_attributes']
        tq_df = df['temperature']
        # city_df['Latitude'] = city_df['Latitude'].astype("object")
        # print(city_df.dtypes)
        city_row = city_df.shape
        city_name = None
        for i in range(0, city_row[0]):
            Latitude = city_df.loc[i, 'Latitude']
            Longitude = city_df.loc[i, 'Longitude']
            if str(Latitude) == str(lat):
                if str(Longitude) == str(lon):
                    city_name = city_df.loc[i, 'City']
                    break
        tq_row = tq_df.shape
        #  格式化时间
        wz1 = dt.find("年")
        y = dt[:wz1]
        wz2 = dt.find("月")
        m = dt[wz1 + 1:wz2]
        wz3 = dt.find("日")
        d = dt[wz2 + 1:wz3]
        wz4 = dt.find("时")
        h = dt[wz3 + 1:wz4]
        gshrq = y + "-" + m + "-" + d + " " + h + ":00:00"
        wd = 0.0
        for i in range(0, tq_row[0]):
            rq = tq_df.loc[i, 'datetime']
            if str(rq) == gshrq:
                wd = tq_df.loc[i, city_name]
                break
        return wd


S = Solution()
print(S.weather_searching(42.358429, -71.059769, "2017年01月09日19时"))
