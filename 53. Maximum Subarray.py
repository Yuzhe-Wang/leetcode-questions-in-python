'''idea: remove negative prefix'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        result = nums[0]
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            result = max(result, curr)
        return result