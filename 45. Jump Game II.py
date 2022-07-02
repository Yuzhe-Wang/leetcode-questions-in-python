class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            val = nums[i]
            minStep = dp[i+1]
            for j in range(i+1, min((len(nums)-1), i+val)+1):
                if dp[j] < minStep:
                    minStep = dp[j]
            dp[i] = minStep + 1
        return dp[0]
    '''
    idea: dynamic programming
    '''