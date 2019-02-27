# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 11:50
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 283. Move Zeroes.py
# @Software: PyCharm
from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                zero_pos = i
                for j in range(zero_pos + 1, l):
                    if nums[j] != 0:
                        nums[zero_pos], nums[j] = nums[j], nums[zero_pos]
                        break

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        i = 0
        for k in nums:
            if k == 0:
                s += 1

        while i < len(nums) - s:
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                continue
            i += 1

    def moveZeroes3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for j in range(count, len(nums)):
            nums[j] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if k != i:
                    nums[k], nums[i] = nums[i], nums[k]
                k += 1

if __name__ == '__main__':
    A = [0, 1, 0, 0,3, 12]
    Solution().moveZeroes(A)
    print(A)
