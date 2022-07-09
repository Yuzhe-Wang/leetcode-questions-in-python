# solution #1: dfs + early stopping
# which will still TLE for cases like "11111111111111111111"
class Solution:
    def numDecodings(self, s: str) -> int:
        result = 0
        result = self.dfs(s, 0, 0)
        return result
    
    def dfs(self, s, result, start):
        # base case:
        if start == len(s):
            return 1
        
        # recurrsive step:
        for i in range(start, len(s)):
            if s[start] == '0':
                break
            temp = int(s[start:i+1])
            if temp >=1 and temp <= 26:
                result += self.dfs(s, 0, i+1)
        return result

# solution #2: dynamic programming
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        n = len(s)
        
        #base cases:
        if int(s[n-1]) in range(1,27):
            dp[n-1] = 1
        dp[n] = 1
            
        # populate the rest of the array
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] += dp[i+1]
                if (i+1 <= len(s) and int(s[i:i+2]) in range(1,27)):
                    dp[i] += dp[i+2]
                
        return dp[0]