class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)+1
        # remember to sort nums, otherwise we cannot disallow same number on the same layer
        nums.sort()
        for i in range(n):
            self.dfs(nums, [], result, 0, i)
        return result
    
    def dfs(self, nums, curr, result, index, n):
        # base case:
        if n == 0:
            result.append(curr.copy())
            return
        
        # recurrsive step
        for i in range(index, len(nums)):
            # disallow the same numbers on the same layers
            if i > index and nums[i] == nums[i-1]:
                continue
            curr.append(nums[i])
            self.dfs(nums, curr, result, i+1, n-1)
            curr.pop()