# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 10:32
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 7. Reverse Integer.py
# @Software: PyCharm
from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        if temp[0] == '-':
            temp = '-' + temp[1:][::-1]
        else:
            temp = temp[::-1]
        if int(temp) < - 2 ** 31 or int(temp) > 2 ** 31 - 1:
            return 0
        else:
            return int(temp)


if __name__ == '__main__':
    A = -123
    print(Solution().reverse(A))
