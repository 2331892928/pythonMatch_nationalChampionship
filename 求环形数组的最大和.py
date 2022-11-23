"""
任务详情
给定一个由整数构成的环形数组 arr，求环形数组的非空子数组的最大和。
环形数组意味着数组的头部和尾部是相连接的，如：[1, 3, 5, 4, 2]

http://zxbs.itmc.cn/jsnlpythoncw1/static/data/ueditor/image/20221028/1666944293871008857.png

任务要求
程序接收整数类型构成的数组 arr，返回结果为整数类型；

数组中的数字包含：正整数、负整数和 0。

测试用例
输入：[1, 3, 5, 4, 2]
输出：15
解释：由于数组是环形，最大子数组是 [1, 3, 5, 4, 2]，子数组之和是 15；

输入：[-1, 9, -6, -1, -5]
输出：9
解释：最大子数组是 [9]，子数组之和是 9；

输入：[8, -10, 10, -1, 6, -8]
输出：15

"""


# -*- coding: utf-8 -*-
# 1. 运行或提交代码不需要自己编写测试用例，后台自动进行测试检查。
# 2. 您编写代码的区域需要限制在Solution类或其他类和函数体内，保证输入与输出符合任务要求即可。
# 3. 点击“提交代码”按钮，系统将查看程序是否正确，并保存代码，记录任务数据。
# 4. 提交代码次数越多，任务得分越低。
# 5. 点击右上方“结束任务”按钮，系统将在后台计算任务得分，任务结束。
class Solution:

    def circular_arr_sum(self, arr: list) -> int:
        """

        :param arr:
        :return:
        """
        """思路：分为两种情况：

（1）无环，直接遍历

（2）有环:

  注意 : 

       1.只有三个以及以上元素才会存在环

       2.数组所有元素和sum是一个定值,环必定经过nums[0]和nums[n-1];

       3.设min=1~n-1范围内最小的和，由于sum和不变，所以，环形子数组最大值=sum-min;

        所以，我们不用关心起点，终点的索引。我们只需要关心局部连续最小值就可以,注意这个局 

      部的意思是1~n-1哦"""
        #  判断是否环形
        arr1 = arr.copy()
        arr1.sort()
        pre = 0
        ans = arr1[0]
        for i in arr1:
            pre = max(pre + i, i)
            ans = max(ans, pre)
        if len(arr) <= 2:
            return ans

        cj = arr1[0] - arr1[len(arr1) - 1]
        if len(arr1) - 1 == cj:
            #  是环形
            return sum(arr1)
        #  不是环形
        n = len(arr1)
        min1 = arr1[0]
        max1 = arr1[n - 1]
        sumnumber = sum(arr)
        dp = []
        for i in arr1:
            min1 = min(min1, i)
        ans2 = sumnumber - min1

        return max(ans, ans2)


S = Solution()
print(S.circular_arr_sum([1, 3, 5, 4, 2]))
