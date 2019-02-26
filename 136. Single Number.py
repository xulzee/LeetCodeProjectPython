# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 17:52
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 136. Single Number.py
# @Software: PyCharm

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == '__main__':
    A = [4,1,2,1,2]
    print(Solution().singleNumber(A))
