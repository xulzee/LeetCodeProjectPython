# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 17:02
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 217. Contains Duplicate.py
# @Software: PyCharm
from typing import List


class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

    def containsDuplicate(self, nums: List[int]) -> bool:
        A = set()
        for i in nums:
            if i not in A:
                A.add(i)
            else:
                return True
        return False

if __name__ == '__main__':
    A = [1, 2, 3, 3, 4, 5, 6, 7]
    print(Solution().containsDuplicate(A))

