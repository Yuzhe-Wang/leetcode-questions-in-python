class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        self.dfs(nums, curr, result)
        return result
        
    def dfs(self, nums, curr, result):
        # base case
        if len(nums) == 0:
            result.append(curr.copy())
            return result
        
        # recurrsive step
        for i in range(len(nums)):
            curr.append(nums.pop(i))
            self.dfs(nums, curr, result)
            nums.insert(i, curr.pop())