class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for n in range(len(nums)+1):
            curr = []
            self.helper(nums, n, 0, curr, result)
        return result
    
    def helper(self, nums, n, k, curr, result):
        # base case:
        if k == n:
            result.append(curr.copy())
            return
        
        # recurrsive step:
        for i in range(k,n):
            curr.append(nums[i])
            self.helper(nums, n, i+1, curr, result)
            curr.pop()