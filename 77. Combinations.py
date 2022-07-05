class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        curr = []
        self.helper(n, k, 1, curr, result)
        return result

    def helper(self, n, k, i, curr, result):
        # base case:
        if k == 0:
            result.append(curr.copy())
            return
        
        # recurrsive step
        for x in range(i, n+1):
            curr.append(x)
            self.helper(n, k-1, x+1, curr, result)
            curr.pop()