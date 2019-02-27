# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:57
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 1. Two Sum.py
# @Software: PyCharm
from typing import List


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     if (target - nums[i]) in nums[i+1:]:
        #         return [i, i + 1 + nums[i+1:].index(target - nums[i])]

        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index


if __name__ == '__main__':
    A = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(A, target))
