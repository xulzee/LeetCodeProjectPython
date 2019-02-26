# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 11:47
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 26. Remove Duplicates from Sorted Array.py
# @Software: PyCharm
from typing import List


class Solution:
    # pop
    def removeDuplicates1(self, nums: List[int]) -> int:
        j = 0
        remove_list = []
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                remove_list.append(i)
            j = i
        # print(remove_list)
        for i in remove_list[::-1]:
            nums.pop(i)
        return len(nums)

    # swap
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        if len(nums) > 0:
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]:
                    nums[j] = nums[i]
                    j += 1
        else:
            j = 0
        return j


if __name__ == '__main__':
    A = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(A))
    print(A)
