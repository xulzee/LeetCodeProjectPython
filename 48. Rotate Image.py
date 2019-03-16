# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 16:02
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 48. Rotate Image.py
# @Software: PyCharm
from typing import List


class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = matrix[i][::-1]

    def rotate(self, matrix: List[List[int]]) -> None:
        start_row, start_column = 0, 0
        end_row, end_column = len(matrix) - 1, len(matrix) - 1
        while start_row < end_row:
            self.rotateEdge(matrix, start_row, start_column, end_row, end_column)
            start_row += 1
            start_column += 1
            end_row -= 1
            end_column -= 1

    def rotateEdge(self, matrix: list, start_row: int, start_column: int, end_row: int, end_column: int) -> None:
        times = end_row - start_row
        for i in range(times):
            temp = matrix[start_row][start_column + i]
            matrix[start_row][start_column + i] = matrix[end_row - i][start_column]
            matrix[end_row - i][start_column] = matrix[end_row][end_column - i]
            matrix[end_row][end_column - i] = matrix[start_row + i][end_column]
            matrix[start_row + i][end_column] = temp


if __name__ == '__main__':
    A = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    # Solution().rotate(A)
    Solution().rotate(A)
    print(A)
