"""
任务详情
下方给定一工作簿 random_num.xlsx，random_num.xlsx 由 20 个工作表组成，要求计算 20 个表中所有数字之和。

任务要求
程序不接收输入参数，返回结果的数据类型是 int；

该道题目结果唯一，不提供准确测试用例。

测试用例
示例如下：

工作表 'ybof' 所有数字的和是 1441；

工作表 'kbkva' 所有数字之和是 996；

依次类推，可以算出 20 个工作表中各个表所有数字之和；

最后将 20 个工作表所得到的 20 个数字求和，即可得到正确结果。

附件信息
random_num.xlsx。信息如下：

工作簿的名称由多个随机小写字母组成；

工作表由一组数据和该组数组的行索引和列索引组成，行索引从 0 开始，列索引由单个小写字母组成；

工作簿的第一列是索引，请勿将其作为一列数据使用；

工作表的数据规模可能不同。

http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/261/fj_random_num.xlsx


"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
import pandas as pd
import requests


class Solution:

    def random_num_in_sheet(self) -> int:
        df = pd.read_excel("http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/261/fj_random_num.xlsx",sheet_name=None)
        sum2 = 0
        for sheetname,datas in df.items():
            # print(sheetname)

            sum1 = datas.sum()
            sum1[0] = 0
            sum2 = sum2 + sum(sum1)
            # print(sum(sum1))
        return sum2

S = Solution()
print(S.random_num_in_sheet())
