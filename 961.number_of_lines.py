# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 961.number_of_lines.py
# @Software: PyCharm


import math
class Solution:
    def numberOfLines1(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        count = 0
        for i in S:
            if count % 100 + widths[ord(i) - 97] > 100:
                count = math.ceil(count / 100) * 100 + widths[ord(i) - 97]
            else:
                count += widths[ord(i) - 97]
        return [math.ceil(count / 100), count % 100]

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        linewidth = 0
        ord_a = ord('a')
        for ch in S:
            width = widths[ord(ch) - ord_a]
            linewidth += width
            if linewidth > 100:
                lines += 1
                linewidth = width
        return [lines, linewidth]


if __name__ == '__main__':
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "abcdefghijklmnopqrstuvwxyz"
    print(Solution().numberOfLines(widths, S))
