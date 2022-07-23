class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMin , currMax = 1, 1
        
        for n in nums:
            temp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp, currMin * n, n)
            result = max(result, currMax)
        return result