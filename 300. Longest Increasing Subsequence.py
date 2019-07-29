class Solution:
    # 当前指向的数字
    def process(self, nums, cur):
        if cur == 0:
            return 1

        ret = 1
        for i in range(cur, -1, -1):
            if nums[i] < nums[cur]:
                ret = max(ret, self.process(nums, i) + 1)

        return ret

    def dynamicProcess(self, nums):
        dp = [0] * len(nums)
        dp[0] = 1
        res = 0
        for i in range(len(nums)):
            ret = 1
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    ret = max(ret, dp[j] + 1)
            dp[i] = ret
            res = max(res, dp[i])
        return res

