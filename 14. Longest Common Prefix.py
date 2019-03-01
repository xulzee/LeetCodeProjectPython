# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 16:53
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 14. Longest Common Prefix.py
# @Software: PyCharm
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix


if __name__ == '__main__':
    # A = ["a","b"]
    # A = ["flower", "flow", "flight"]
    # A = []

    A = ["aa", "a"]
    print(Solution().longestCommonPrefix(A))
