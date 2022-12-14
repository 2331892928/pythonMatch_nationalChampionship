"""
任务说明
读取给定的职工薪酬考勤簿，职工薪酬考勤簿由两个表格组成，分别是 基本薪资 工作表和 上班通勤 工作表。要求计算每一个部门内部的平均薪资，并把结果 降序 排列，返回给判定程序。

员工个人薪酬计算过程如下：

薪资由两部分组成， 月基本薪资 和 通勤工资，另外需要扣除需要缴纳的 五险一金；

月基本薪资 = 基本薪资+岗位工资 + 绩效工资；

通勤工资中计算如下：

日薪 = (基本薪资 + 岗位工资 + 绩效工资) / 应出勤天数
时薪 = 日薪 / 8

比如小王基本薪资+岗位工资+绩效工资共计5000，应出勤22天，日薪=227.27..，时薪=28.4090…

通勤工资中，法定节假日加班薪资是工作日加班的 2 倍，周末加班工资是工作日加班的 1.5 倍，工作日加班工资与时薪 相同；

通勤工资需要扣除因请假导致的缺勤，

请假/小时需要扣除的工资按照时薪计算。

如小王时薪是20，请假2天，需要扣除的工资是 20 * 2 * 8 = 320；

五险一金个人缴费按照社会保险缴费基数计算。

养老保险个人缴费比例是 8%

医疗保险个人缴费比例是 2%

失业保险个人缴费比例是 1%

公积金缴费比例是 10%

某员工个人缴费基数是 2000，养老保险 2000 * 0.08 = 160，医疗保险 2000 * 0.02 = 40，失业保险 2000 * 0.01 = 20，公积金 2000 * 0.1 = 200，个人合计承担五险一金费用 420。

示例：
小王基本工资 2000，岗位工资 2000，社会保险缴费基数是 2000。绩效工资 0，应出勤天数 20 天，请假 1 天，工作日加班 8 小时，法定节假日加班 4 小时，周末加班 4 小时。

小王基本薪资+岗位工资+绩效工资是：2000 + 2000 = 4000；
小王时薪：4000 / 20 / 8 = 25；
小王加班工资：25 * 8 + 25 * 4 * 1.5 + 25 * 4 * 2 = 550；
小王请假扣除：25 * 8 = 200；
小王五险一金扣除：2000 * 0.08 + 2000 * 0.02 + 2000 * 0.01 + 2000 * 0.1 = 420；
小王本月实发工资：4000 + 550 - 200 - 420 = 3930。

假设小王所在部门有 5 个人，5 个人工资分别是 4050，4010，4120，4000，4500。小王所在部门的平均工资是：(3930+ 4010 + 4120 + 4000 + 4500) /5 = 4112。同理可算出其他部门的平均工资。



注意：返回结果需四舍五入保留小数点后两位！

返回结果参数类型是 pd.Series。Series 的索引应为部门名，Series 的数据应为部门平均工资，Series 的 Name 属性应修改为 “平均薪资”。

任务要求
程序无需接收参数输入，需要返回结果参数的格式是 pd.Series；

返回结果时需要四舍五入保留小数点后两位，计算过程内保留小数点后两位可能导致最后结果不正确；

部门平均工资需要降序排列；

本题所需的基本薪资表和上班通勤表均在职工薪酬工作簿中，按需读取。

Series 数据的类型应为 float 64，Name 属性应为 “平均薪资”。

index 的属性名应为部门。

测试用例
部分返回数据：

部门
销售部       15767.86
运营部       ****
工程部       ****
财务部       ****
研发部       ****
市场部       ****
人力资源部    4233.27
Name: 平均薪资, dtype: float64
附件信息
职工薪酬簿.xlsx，职工薪酬工作簿由 基本薪资 工作表和 上班通勤 工作表组成。

基本薪资工作表。基本薪资工作表包含个人所属部门，各部分薪资状况和社会保险缴纳基数。共 7 个部门共 50 条数据，其中只有销售部有绩效工资。

上班通勤工作表。上班通勤工作表包含本月应出勤天数，实际出勤天数。请假加班天数等。工作表中的名字与基本薪资工作表中的名字一一对应。共 50 条数据。

http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/258/fj_9210_employee_salary_work_books.xlsx

"""
# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
import pandas as pd


class Solution:

    def department_salary_summary(self) -> pd.Series:
        df = pd.read_excel(
            "http://zxbs.itmc.cn:80/jsnlpythoncw1/data/user/14746/258/fj_9210_employee_salary_work_books.xlsx",
            sheet_name=None)
        jbxz_df = df['基本薪资']
        sbtq_df = df['上班通勤']
        sbtq_df['法定假日加班（小时）'] = sbtq_df['法定假日加班（小时）'].fillna(0)
        sbtq_df['周末加班（小时）'] = sbtq_df['周末加班（小时）'].fillna(0)
        sbtq_df['工作日加班（小时）'] = sbtq_df['工作日加班（小时）'].fillna(0)
        sbtq_df['请假（小时）'] = sbtq_df['请假（小时）'].fillna(0)
        bm = {}
        jbxz_row = jbxz_df.shape
        sbtq_row = sbtq_df.shape
        var1 = None
        for i in range(0, jbxz_row[0]):
            var = jbxz_df.loc[i, ['部门', '姓名', '基本薪资', '岗位工资', '绩效工资', '社会保险缴费基数']]
            for j in range(0, sbtq_row[0]):
                var1 = sbtq_df.loc[j]
                name = str(var1['姓名'])
                if name == str(var[1]):
                    break

            rx = float(var[2]) + float(var[3]) + float(var[4]) / int(var1['应出勤天数（天）'])
            #  时工资
            sx = rx / 8
            #  请假扣除
            qjkc = sx * (float(var1['请假（小时）']))
            #  加班工作日
            jqbzr = float(var1['工作日加班（小时）']) * sx
            #  节假日加班
            jjrjb = float(var1['法定假日加班（小时）']) * (sx * 2)
            #  周末加班
            zmjb = float(var1['周末加班（小时）']) * (sx * 1.5)
            #  缴费基数
            jfjs1 = float(var[5])
            jfjs = jfjs1 * 0.08 + jfjs1 * 0.02 + jfjs1 * 0.01 + jfjs1 * 0.1
            #  实发工资
            sfgz = (float(var[2]) + float(var[3]) + float(var[4])) + jqbzr + jjrjb + zmjb - qjkc - jfjs
            sfgz = round(sfgz, 2)
            if var[0] not in bm:
                bm[var[0]] = {
                    "sfgz": 0.0,
                    "rs": 0
                }
            bm[var[0]] = {
                "sfgz":bm[var[0]]['sfgz'] + sfgz,
                "rs":bm[var[0]]['rs'] + 1
            }
        print(bm)



S = Solution()
S.department_salary_summary()
