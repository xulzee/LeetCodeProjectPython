# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 521.longest-uncommon-subsequence-i.py
# @Software: PyCharm


class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        len_a = len(a)
        len_b = len(b)
        if len_a == len_b:
            if a == b:
                return -1
            else:
                return len_a
        else:
            return max(len_a, len_b)


if __name__ == '__main__':
    a = 'aba'
    b = 'cbc'
    print(Solution().findLUSlength(a, b))
