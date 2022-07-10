class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        # base cases:
        dp[0] = 1
        dp[1] = 1
        
        # fill the rest of the array
        for i in range(2, n+1):
            # try all possible roots
            for j in range(1, i+1):
                # number of BSTs = number of left subtrees * number of right subtrees
                dp[i] += dp[j-1] * dp[i-j]
                
        return dp[n]