class Solution:
    def process(self, m, n, i, j):
        if i == m and j == n:
            return 1
        if i == m:  # 在最右一列
            return self.process(m, n, i, j + 1)
        if j == n:  # 在最下一行
            return self.process(m, n, i + 1, j)
        # 一般情况
        return self.process(m, n, i + 1, j) + self.process(m, n, i, j + 1)

    def dynamicProcess(self, m, n):
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n, 0, -1):
            for j in range(m, 0, -1):
                if i == n and j == m:
                    dp[i][j] = 1
                elif i == n:
                    dp[i][j] = dp[i][j + 1]
                elif j == m:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j]

        return dp[1][1]


if __name__ == '__main__':
    print(Solution().dynamicProcess(7, 3))
