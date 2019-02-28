# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 14:03
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 387. First Unique Character in a String.py
# @Software: PyCharm
from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for j in range(len(s)):
            if hashmap[s[j]] == 1:
                return j
        return -1

if __name__ == '__main__':
    A = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(A, target))
