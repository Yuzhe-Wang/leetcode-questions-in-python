class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        temp = []
        self.helper(candidates, target, 0, temp, result)
        return result
    
    def helper(self, candidates, target, curr, temp, result):
        # base case:
        if target == 0:
            result.append(temp.copy())
            return result
        
        # recurrsive step
        for i in range(curr, len(candidates)):
            # disallow same choice on the same level
            if i > curr and candidates[i] == candidates[i-1]:
                 continue
            if candidates[i] <= target:
                temp.append(candidates[i])
                self.helper(candidates, target-candidates[i], i+1, temp, result)
                del temp[-1]