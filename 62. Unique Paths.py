class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        # base cases:
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                temp = 0
                if i < m-1:
                    temp += dp[i+1][j]
                if j < n-1:
                    temp += dp[i][j+1]
                dp[i][j] = temp
        return dp[0][0]