# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 15:21
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 189. Rotate Array.py
# @Software: PyCharm
from typing import List


class Solution(object):
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = len(nums)
        # k %= l
        # nums[:l-k] = nums[:l-k][::-1]
        # nums[l-k:] = nums[l-k:][::-1]
        # nums[:] = nums[::-1]
        l = len(nums)
        k %= l
        nums[:l] = nums[:l][::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:l] = nums[k:l][::-1]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(A, k)
    print(A)
