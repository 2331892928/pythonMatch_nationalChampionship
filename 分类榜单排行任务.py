"""
任务说明
根据要求完成下面的任务：

根据指定的具体关键词 (kw) 查找对应的榜单名；

根据指定的榜单名称 (name) 和关键词排名 (rank) 查找对应的关键词。

返回由题目一中榜单名和题目二中关键词组成的列表，榜单名在前，关键词在后，不可调换顺序。

任务要求
程序接收三个变量，分别为 kw、name 和 rank，其对应的数据类型分别为 str、str 和 int；

程序返回结果的数据类型为 list。

测试用例
示例一
输入：kw = '广州', name = '旅游城市', rank = 1
输出：['旅游城市', '广州']
解释：关键词 '广州' 在旅游城市榜单中，旅游城市 排名第 1 的是 '广州'

示例二
输入：kw = '深圳', name = '手机', rank = 10
输出：['旅游城市', '一加手机']
解释：关键词 '深圳' 在旅游城市榜单中，手机 榜单中排名第 10 的是 '一加手机'

示例三
输入：kw = '五台山', name = '风景名胜', rank = 4
输出：['风景名胜', '九寨沟']
http://zxbs.itmc.cn:80/jsnlpythoncw1/open/show/banner/index.html

这题做过，略过
"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
from typing import List

import requests
from bs4 import BeautifulSoup


class Solution:

    def list_display(self, kw: str, name: str, rank: int) -> List[str]:
        pass