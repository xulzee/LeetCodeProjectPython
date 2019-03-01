# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 10:19
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 28. Implement strStr().py
# @Software: PyCharm
from typing import List


class Solution:
    def get_next(self, s: str) -> List[int]:
        next_list = [-1] * len(s)
        i = 0
        j = -1
        while i < len(s) - 1:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                next_list[i] = j
            else:
                j = next_list[j]
        return next_list

    def strStr(self, haystack: str, needle: str) -> int:
        next_list = self.get_next(needle)
        j = 0
        i = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                j = next_list[j]
        if j == len(needle):
            return i - j
        else:
            return -1
    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        len_h = len(haystack)
        len_n = len(needle)

        for i in range(len_h):
            if i + len_n > len_h:
                return -1

            if haystack[i] == needle[0]:
                if haystack[i:len_n+i] == needle:
                    return i

        return -1

if __name__ == '__main__':
    haystack = "ababc"
    needle = "issip"
    print(Solution().strStr(haystack, needle))
