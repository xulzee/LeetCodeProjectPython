# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:46
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 509.fibonacci-number.py
# @Software: PyCharm


class Solution:
    def fib1(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Too Slow because Function call overhead
        if N is 0:
            return 0
        if N is 1:
            return 1
        return self.fib(N - 1) + self.fib(N - 2)

    def fib2(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        fn, fn_1, fn_2 = 0, 1, 0
        while N >= 2:
            fn = fn_1 + fn_2
            fn_1, fn_2 = fn, fn_1
            N -= 1
        return fn

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        stack = [0, 1]
        while N >= 2:
            stack.append(stack[-1] + stack[-2])
            N -= 1
        return stack[-1]


if __name__ == '__main__':
    N = 5
    print(Solution().fib(N))

