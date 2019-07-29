class Solution:
    '''
    w : 物品重量
    v : 物品价值
    c : 剩余重量
    i ：前i个物品
    '''
    def process(self, w, v, c, i):
        if i < 0:
            return 0
        if c >= w[i]:  # 可以放进背包
            return max(self.process(w, v, c - w[i], i - 1) + v[i], self.process(w, v, c, i - 1))
        else:  # 剩余容量不能放进背包
            return self.process(w, v, c, i - 1)

    def dynamicProcess(self, w, v, c):
        dp = [[0] * len(w) for j in range(c + 1)]

        for i in range(1, c + 1):
            for j in range(1, len(w)):
                if i >= w[j]:
                    dp[i][j] = max(dp[i - w[j]][j - 1] + v[j], dp[i][j - 1])

        return dp[-1][-1]



if __name__ == '__main__':
    print(Solution().dynamicProcess([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 10))
