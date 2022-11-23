"""任务详情
观察下方给出的页面，统计页面中指定颜色色块的数量。

任务要求
1. 程序接受颜色变量 keyword，str 数据类型，返回一个整数 int 类型的色块数量；

2. 如果网页没有该颜色，返回 0，颜色变量 keyword 不区分大小写；

3. 所需网页在下方给出，页面编码方式为utf-8。

测试用例
输入：'red'
输出：51

解释：网页中红色色块（red）的数量是 51。


输入：'pine-red'
输出：0

解释：网页中酒红色色块（pine-red）的数量是 0。



输入：'blue'

输出：39

http://zxbs.itmc.cn:80/jsnlpythoncw1/open/show/simple_color_page.html
"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
import re

import requests
import bs4


class Solution:

    def simpleColor(self, keyword: str) -> int:
        res = requests.get("http://zxbs.itmc.cn:80/jsnlpythoncw1/open/show/simple_color_page.html")
        res_txt = res.content.decode()
        soup = bs4.BeautifulSoup(res_txt, "html.parser")
        sum1 = 0
        for i, v in enumerate(soup.find_all("div")):
            style = v['style']
            wz1 = str(style).find(": ")
            wz2 = str(style).find(";")
            if str(style)[wz1+2:wz2] == keyword:
                sum1 = sum1 + 1
        return sum1


S = Solution()
print(S.simpleColor("red"))
