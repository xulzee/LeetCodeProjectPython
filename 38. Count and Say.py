# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 14:34
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 38. Count and Say.py
# @Software: PyCharm
class Solution:
    def countAndSay1(self, n: int) -> str:
        if n == 1:
            return "1"

        result = self.countAndSay(n - 1)

        i = result[0]
        count_i = 1
        temp = ""
        for j in range(1, len(result)):
            if result[j] == i:
                count_i += 1
            else:
                temp = temp + str(count_i) + str(i)
                count_i = 1
                i = result[j]
        temp = temp + str(count_i) + str(i)
        return temp

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        pre = "11"
        for i in range(3,n+1):
            temp = ""
            count = 1
            count_char = pre[0]
            for j in range(1, len(pre)):
                if count_char == pre[j]:
                    count += 1
                else:
                    temp = temp + str(count) + str(count_char)
                    count_char = pre[j]
                    count = 1
            temp = temp + str(count) + str(count_char)
            pre = temp
        return pre




if __name__ == '__main__':
    for n in range(1, 21):
        print(Solution().countAndSay(n))
