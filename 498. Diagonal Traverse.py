# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 16:56
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 498. Diagonal Traverse.py
# @Software: PyCharm
class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0:
            return []
        horizon_column = 0
        horizon_row = 0
        vertical_column = 0
        vertical_row = 0
        end_row = len(matrix) - 1
        end_column = len(matrix[0]) - 1
        flag = True
        res = []
        while horizon_column <= end_column and horizon_row <= end_row:
            self.printLevel(matrix, horizon_row, horizon_column, vertical_row, vertical_column, flag, res)
            if horizon_column == end_column:
                horizon_row += 1
            else:
                horizon_column += 1
            if vertical_row == end_row:
                vertical_column += 1
            else:
                vertical_row += 1
            flag = not flag
        return res

    def printLevel(self, matrix, horizon_row, horizon_column, vertical_row, vertical_column, flag, res):
        if flag is True:
            while vertical_column <= horizon_column:
                res.append(matrix[vertical_row][vertical_column])
                vertical_row -= 1
                vertical_column += 1
        else:
            while horizon_column >= vertical_column:
                res.append(matrix[horizon_row][horizon_column])
                horizon_row += 1
                horizon_column -= 1


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[2,3]]
    print(Solution().findDiagonalOrder(matrix))
