# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 9:57
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 344. Reverse String.py
# @Software: PyCharm
from typing import List


class Solution:
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range((l - 1) // 2 + 1):
            s[i], s[l - i - 1] = s[l - i - 1], s[i]


if __name__ == '__main__':
    A = [2, 7, 11, 15]
    Solution().reverseString(A)
    print(A)
