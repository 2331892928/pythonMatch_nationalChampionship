"""
任务要求
统计网页中所有数字之和，网页共有 100 个，每一页存在 100 个数字。

给定两个参数 page_num 和 position_num，page_num 是一个整数，position_num 是
一个整数。page_num 表示需要寻找的页数，position_num 表示需要寻找的位置。

请你编写程序，寻找到 page_num 中第 position_num 的数字。

例如：page_num=2，position=10 结果是 747
第 2 页第 10 个数字是 747

任务说明
程序接收 参数 page_num 是 int 类型，position_num 是 int 类型；

程序需要读取网页数据；

返回结果的数据类型也是整数类型。

判定程序确保提供的参数存在于页面中，即 1<=page_num<=100，1<=position_num<=100。

测试用例
输入：page_num=5, position_num=53

输出：913
解释：第5页，第53个数字是913

输入：page_num=29，position_num=5
输出：961

解释：第29页，第5个是961

输入：page_num=78, position_num=3

输出：185

http://zxbs.itmc.cn:80/jsnlpythoncw1/open/show/random_number/c426398c-86cd-4bf4-b42c-3049ea13a28a.html

"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
import bs4
from bs4 import BeautifulSoup

import requests


class Solution:
    def task(self, page_num: int, position_num: int) -> int:
        """
        :param page_num: 页码
        :param position_num: 位置代码
        :return: 指定页面中指定位置的数字
        """
        #  题目不存在寻找失败问题，不考虑
        href_prefix = "http://zxbs.itmc.cn:80/jsnlpythoncw1/open/show/random_number"
        href = "./c426398c-86cd-4bf4-b42c-3049ea13a28a.html"
        res = requests.get(href_prefix + href[1:])
        res_txt = res.content.decode()
        soup = bs4.BeautifulSoup(res_txt, "html.parser")
        #  寻找页数的html

        page = soup.find_all(name="ul")
        for i, v in enumerate(page[1].find_all("li")):
            pagenums = v.text
            if int(pagenums) == page_num:
                if v.find("a")['href'] != "#":
                    href = v.find("a")['href']
                break
        res = requests.get(href_prefix + href[1:])
        res_txt = res.content.decode()
        soup = bs4.BeautifulSoup(res_txt, "html.parser")
        page = soup.find_all("ul")
        number = 1
        for i,v in enumerate(page[0].find_all("li")):
            number = v.text
            if position_num == i + 1:
                break
        return number



S = Solution()
print(S.task(29, 5))
