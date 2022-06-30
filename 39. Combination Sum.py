class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        self.helper(candidates, target, 0, curr, result)
        return result
    
    def helper(self, candidates, target, depth, curr, result):
        # base case
        if target == 0:
            result.append(curr.copy())
            return
        # recurrsive step
        for i in range(depth, len(candidates)):
            if candidates[i] <= target:
                curr.append(candidates[i])
                self.helper(candidates, target - candidates[i], i, curr, result)
                del curr[-1]

''' idea: dfs + backtracking, use the variable depth to avoid duplicate combinations'''