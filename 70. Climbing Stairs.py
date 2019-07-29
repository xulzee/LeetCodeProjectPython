class Solution:
    def process(self, n):
        # base case
        if n < 2:
            return 1

        return self.process(n - 1) + self.process(n - 2)

    def dynamicProcess(self, n):
        if n < 2:
            return 1

        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs(self, n):
        return self.dynamicProcess(n)

if __name__ == '__main__':
    print(Solution().climbStairs(3))