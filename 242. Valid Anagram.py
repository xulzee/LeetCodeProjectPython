# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 14:55
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 242. Valid Anagram.py
# @Software: PyCharm
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 26
        l_s = len(s)
        l_t = len(t)
        if l_s != l_t:
            return False
        else:
            ord_a = ord('a')
            for i in range(l_s):
                s_list[ord(s[i]) - ord_a] += 1
                s_list[ord(t[i]) - ord_a] -= 1
            for j in s_list:
                if j != 0:
                    return False
            return True



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
