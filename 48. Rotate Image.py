# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 16:02
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 48. Rotate Image.py
# @Software: PyCharm
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = matrix[i][::-1]


if __name__ == '__main__':
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(A)
    print(A)
