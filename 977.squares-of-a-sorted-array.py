# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 977.squares-of-a-sorted-array.py
# @Software: PyCharm


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):
            A[i] = A[i] ** 2
        return sorted(A)


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(A))
