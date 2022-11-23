"""
任务详情
后台传入两个数组 li 和 sub_li，编写一个程序检查 sub_li 是否为 li 的子数组。
如果 sub_li 是 li 的子数组， 返回 True，否则返回 False。

例如：li = [1, 2, 4, 2], sub_li = [2, 4], li 中包含 sub_li，返回 True。
li = [3, 5, 1, 2], sub_li = [3, 1], li 不包含 sub_li, 返回 False。

任务要求
程序接收参数 li 和 sub_li 为 list 数据类型；

程序返回结果为 bool 数据类型；

注意：如果 li 中的元素和 sub_li 中的元素相同，则 sub_li 不属于 li 的子数组；

子数组包含元素顺序，如 [1, 2] 是 [1, 2, 3, 4] 的子数组，[2, 1] 不是 [1, 2, 3, 4] 的子数组。

测试用例
输入：li = [8, 7, 7, 1, 8], sub_li = [7, 7, 1]
输出：True
解释：[7, 7, 1] 是 [8, 7, 7, 1, 8] 的子数组，也就是 [8, 7, 7, 1, 8] 包含有 [7, 7, 1]，结果返回 True；

输入：li = [3, 8, 7, 2, 5, 2], sub_li = [3, 6, 4]
输出：False
解释：sub_li 不是 li 的子数组，返回 False；

输入：li = [7, 7, 7], sub_li = [7, 7, 7]
输出：False
解释：li 和 sub_li 完全相等，也就是 sub_li 不是 li 的子数组。
"""

# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
from typing import List


class Solution:

    def is_sublist(self, li: List[int], sub_li: List[int]) -> bool:
        """
        :param li: 父数组
        :param sub_li: 子数组
        :返回两者关系
        """
        a = ""
        for i in li:
            if a == "":
                a = str(i)
            else:
                a = a + "," + str(i)
        b = ""
        for i in sub_li:
            if b == "":
                b = str(i)
            else:
                b = b + "," + str(i)
        if a.find(b) == -1:
            return False
        else:
            return True


S = Solution()
print(S.is_sublist([3, 8, 7, 2, 5, 2], [3, 6, 4]))
