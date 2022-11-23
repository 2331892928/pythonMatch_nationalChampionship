"""
任务详情
根据下方的企业产品销售基础数据工作簿，计算指定品类所有产品毛利率变动的平均值。

毛利率 = (收入 - 成本) / 收入

毛利率变动 = 本期毛利率 - 上期毛利率

任务描述
程序接收 str 类型的变量 name，name 代表的是产品品类；

程序需要返回指定产品品类的毛利率变动平均值，数据类型是 float；

返回结果需四舍五入保留小数点后 4 位，不足 4 位无需补全；

如计算结果类型是 np.float64，需手动将其转换为 float 类型，否则可能导致结果错误。

测试用例
输入：name = '普通水'
结果：0.0207
解释：普通水包含的产品包含纯净水和矿泉水两种。
纯净水上期毛利率是 0.389175..，本期毛利率是 0.414344..，毛利变动率是0.02517；
同理，矿泉水毛利的毛利变动率是0.016273；
两者的平均值是：0.020715，四舍五入结果是：0.0207。

输入：name = '零食'
结果：0.0047
http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/248/fj_enterprise_sales_basic_data.csv

"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
import pandas as pd


class Solution:

    def calculate_mean(self, name) -> float:
        df = pd.read_csv("http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/248/fj_enterprise_sales_basic_data.csv")
        rows = df.shape
        cp_list = []
        for i in range(0, rows[0]):
            cp = df.loc[i, '产品种类']
            if str(cp) == name:
                #  上期
                sq = df.loc[i, ["上期销售收入", "上期销售成本"]]
                sqsr = (float(sq[0]) - float(sq[1])) / float(sq[0])
                #  本期
                bq = df.loc[i, ["本期销售收入", "本期销售成本"]]
                bqsr = (float(bq[0]) - float(bq[1])) / float(bq[0])
                bq = bqsr - sqsr
                cp_list.append(bq)
        a = sum(cp_list) / len(cp_list)
        a = round(a, 4)
        return a


S = Solution()
print(S.calculate_mean("零食"))
