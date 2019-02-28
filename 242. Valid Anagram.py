# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 14:55
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 242. Valid Anagram.py
# @Software: PyCharm
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in s:
                if i not in t:
                    return False
            return True
        else:
            return False

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
