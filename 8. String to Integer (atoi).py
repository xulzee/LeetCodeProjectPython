# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 18:11
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 8. String to Integer (atoi).py
# @Software: PyCharm

class Solution:
    def getnum(self, str: str) -> int:
        nums = ""
        for j in str:
            if not j.isdigit():
                break
            nums += j
        if nums != "":
            nums = int(nums)
        else:
            nums = 0
        return nums

    def myAtoi(self, str: str) -> int:
        if str == "":
            return 0

        INT_MAX = 0x7fffffff
        INT_MIN = -0x80000000

        # 去前缀空
        for i in range(len(str)):
            if str[i] != " ":
                str = str[i:]
                break

        nums = ""
        if str[0] == "-":
            nums = self.getnum(str[1:])
            nums = -nums
        elif str[0] == "+":
            nums = self.getnum(str[1:])
        elif str[0].isdigit():
            nums = self.getnum(str)
        else:
            return 0

        if nums == "":
            return 0
        #
        if nums <= INT_MIN:
            return INT_MIN
        if nums >= INT_MAX:
            return INT_MAX

        return nums


if __name__ == '__main__':
    A = "    0000000000000   "
    print(Solution().myAtoi(A))
