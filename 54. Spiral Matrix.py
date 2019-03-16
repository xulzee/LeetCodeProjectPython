# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 18:42
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 54. Spiral Matrix.py
# @Software: PyCharm
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        start_row, start_column = 0, 0
        end_row, end_column = len(matrix) - 1, len(matrix[0]) - 1
        res = []
        while start_column <= end_column and start_row <= end_row:
            self.printEdge(matrix, start_row, start_column, end_row, end_column, res)
            start_column += 1
            start_row += 1
            end_column -= 1
            end_row -= 1
        return res

    def printEdge(self, matrix: list, start_row: int, start_column: int, end_row: int, end_column: int, res: List):
        if start_row == end_row:
            while start_column <= end_column:
                res.append(matrix[start_row][start_column])
                start_column += 1
        elif start_column == end_column:
            while start_row <= end_row:
                res.append(matrix[start_row][start_column])
                start_row += 1
        else:
            cur_row = start_row
            cur_column = start_column
            while cur_column < end_column:
                res.append(matrix[cur_row][cur_column])
                cur_column += 1
            while cur_row < end_row:
                res.append(matrix[cur_row][cur_column])
                cur_row += 1
            while cur_column > start_column:
                res.append(matrix[cur_row][cur_column])
                cur_column -= 1
            while cur_row > start_row:
                res.append(matrix[cur_row][cur_column])
                cur_row -= 1


if __name__ == '__main__':
    # A = [[5, 1, 9, 11],
    #      [2, 4, 8, 10],
    #      [13, 3, 6, 7],
    #      [15, 14, 12, 16]]
    A = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    res = []
    res = Solution().spiralOrder(A)
    print(res)
