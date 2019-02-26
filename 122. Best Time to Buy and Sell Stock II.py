# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 14:56
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 122. Best Time to Buy and Sell Stock II.py
# @Software: PyCharm
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == '__main__':
    A = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(A))
