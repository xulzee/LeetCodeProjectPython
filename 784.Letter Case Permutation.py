# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 784.Letter Case Permutation.py
# @Software: PyCharm


class Solution:
    def letterCasePermutation(self, S: 'str') -> 'List[str]':
        result = []
        if S == "":
            return [""]
        print(result)
        for i in S:
            if i.isalpha():
                if result == []:
                    result.append(i.lower())
                    result.append(i.upper())
                else:
                    temp = []
                    temp = result[:]
                    for j in range(len(result)):
                        result[j] += i.lower()
                        temp[j] += i.upper()
                    result = result + temp

            else:
                if result == []:
                    result.append(i)
                else:
                    for j in range(len(result)):
                        result[j] += i
        return result


if __name__ == '__main__':
    S = "a1b2"
    print(Solution().letterCasePermutation(S))
