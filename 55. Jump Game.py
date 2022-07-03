class Solution:
    # solution 2: greedy, update the goal constantly runtime complexity O(n)
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        
# solution 1: dynamic programming, runtime complexity O(mn) where m is the max value of the nums and n is the length of the list
#   def canJump(self, nums: List[int]) -> bool:
#         dp = [0] * len(nums)
        
#         # base case:
#         dp[len(nums)-1] = 1
        
#         # populate the array from end to start
#         for i in range(len(nums)-2, -1, -1):
#             curr = nums[i]
#             for j in range(i, min(i + curr + 1, len(nums))):
#                 if dp[j] == 1:
#                     dp[i] = 1
#                     break
            
#         return dp[0]
        