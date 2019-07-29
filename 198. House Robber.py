# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 23:39
# @Author  : xulzee
# @Email   : xulzee@163.com
# @File    : 198. House Robber.py
# @Software: PyCharm


class Solution:
    def process(self, nums, i):  # 偷前面i户人家获取到的最大金额
        # base case
        if i < 0:
            return 0

        return max(nums[i] + self.process(nums, i - 2), self.process(nums, i - 1))

    def dynamicProcess(self, nums):
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return nums[1]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    def rob(self, nums):
        return self.dynamicProcess(nums)


if __name__ == '__main__':
    print(Solution().rob([2, 7, 9, 3, 1]))
