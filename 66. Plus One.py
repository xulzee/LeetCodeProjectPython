# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 11:18
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 66. Plus One.py
# @Software: PyCharm
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        digits[l - 1] += 1
        j = l - 1
        while digits[j] >= 10:
            if j == 0:
                digits[j] = 0
                digits.insert(0, 1)
                return digits
            digits[j] = 0
            j -= 1
            digits[j] += 1
        return digits


if __name__ == '__main__':
    N = [0]
    print(Solution().plusOne(N))
