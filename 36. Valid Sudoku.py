# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 14:38
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 36. Valid Sudoku.py
# @Software: PyCharm
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        column = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                # row
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i][board[i][j]] = 1
                # column
                if board[i][j] in column[j]:
                    return False
                else:
                    column[j][board[i][j]] = 1
                # box
                box_index = (i // 3) * 3 + j // 3
                if board[i][j] in box[box_index]:
                    return False
                else:
                    box[box_index][board[i][j]] = 1
        return True


if __name__ == '__main__':
    A = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(A))
