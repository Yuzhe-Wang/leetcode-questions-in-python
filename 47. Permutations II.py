class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        curr = []
        self.dfs(nums, curr, result)
        return result
    
    def dfs(self, nums, curr, result):
        # base case:
        if len(nums) == 0:
            result.append(curr.copy())
            return result
        
        # recurrsive step
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                curr.append(nums.pop(i))
                self.dfs(nums, curr, result)
                nums.insert(i, curr.pop())
        
        ''' idea: dfs + disallowing same choice at the same level of the decision tree'''