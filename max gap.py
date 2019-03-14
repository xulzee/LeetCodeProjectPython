# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 12:49
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : max gap.py
# @Software: PyCharm

# 给定一个数组，求如果排序之后，相邻两数的最大差值，要求时
# 间复杂度O(N)，且要求不能用非基于比较的排序。
class Solution:
    def maxgap(self, array: list):
        if array == None or len(array) < 2:
            return 0
        array_len = len(array)
        array_max = array[0]
        array_min = array[0]
        for i in array:
            if i >= array_max:
                array_max = i
            if i < array_min:
                array_min = i
        if array_max == array_min:
            return 0
        hasNum = [0] * (array_len + 1)
        maxs = [0] * (array_len + 1)
        mins = [0] * (array_len + 1)
        for j in range(array_len):
            index = self.bucket(array[j], array_len, array_min, array_max)
            if hasNum[index] == 1:
                maxs[index] = max(array[j], maxs[index])
                mins[index] = min(array[j], mins[index])
            else:
                maxs[index] = array[j]
                mins[index] = array[j]
            hasNum[index] = 1

        res = 0
        lastMax = maxs[0]
        for k in range(1, array_len):
            if hasNum[k]==1:
                res = max(res, mins[k] - lastMax)
                lastMax = maxs[k]
        return res

    def bucket(self, num: int, len: int, min: int, max: int):
        return (num - min) * len // (max - min) # 思考

if __name__ == '__main__':
    import random
    test = [random.randint(0, 500) for j in range(10)]
    print(sorted(test))
    print(Solution().maxgap(test))