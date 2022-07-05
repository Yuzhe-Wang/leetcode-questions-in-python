class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        
        # base cases:
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        else:
            dp[m-1][n-1] = 1
        
        # filling the rest of dp
        for k in range(m-1, -1, -1):
            for q in range(n-1, -1, -1):
                if obstacleGrid[k][q] == 1:
                    dp[k][q] == 0 
                else:
                    if k+1 < m:
                        dp[k][q] += dp[k+1][q]
                    if q+1 < n:
                        dp[k][q] += dp[k][q+1]
        
        return dp[0][0]