class Solution:
    '''
    n : 当前为第几年
    '''

    def process(self, n):
        if n == 1 or n == 2 or n == 3 or n == 4:
            return n

        return self.process(n - 1) + self.process(n - 3)

    def dynamicProcess(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in range(5, n + 1):
            dp[i] = dp[i - 1] + dp[i - 3]

        return dp[-1]
