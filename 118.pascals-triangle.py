# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 118.pascals-triangle.py
# @Software: PyCharm


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if numRows == 0:
        #     return []
        output = []
        for row_index in range(numRows):
            current = [0] * (row_index + 1)
            current[0] = 1
            current[row_index] = 1
            for column_index in range(1, row_index):
                current[column_index] = output[row_index-1][column_index-1] + output[row_index-1][column_index]
            output.append(current)
        return output


if __name__ == '__main__':
    N = 0
    print(Solution().generate(N))
