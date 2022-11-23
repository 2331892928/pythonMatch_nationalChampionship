"""
任务详情
给定一个车辆信息网站，要求完成以下指定任务，任务如下：
后台传入车辆的名称 car_name，需要返回该车辆的评分。

任务要求
程序接收 str 类型的变量 car_name，输出结果的数据类型为 float 类型；

如果某车辆暂无评分，则需要返回 '暂无' 字样的字符串。

测试用例
输入：'秦PLUS'                  输出：4.57
解释：秦PLUS 这辆车的评分是 4.57

输入：'Model 3'                输出：4.38
解释：Model 3 这辆车的评分是 4.38

输入：'宋PLUS新能源'        输出：'暂无'

http://zxbs.itmc.cn:80/jsnlpythoncw1/open/show/9785_list_of_cars/index.html
这题做过，略过
"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
import requests
from bs4 import BeautifulSoup


class Solution:

    def list_of_cars(self, car_name: str) -> float:

        pass