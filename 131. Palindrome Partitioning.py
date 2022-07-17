class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # idea: dfs + backtracking
        result = []
        curr = []
        self.dfs(s, curr, result)
        return result
    
    def dfs(self, s, curr, result):
        # base case
        if len(s) == 0:
            result.append(curr.copy())
            return result
        
        # recurrsive steps
        left, right = 0, 1
        while right <= len(s):
            if self.isPalindrom(s[left:right]):
                curr.append(s[left:right])
                self.dfs(s[right:], curr, result)
                curr.pop()
            right+=1
    
    def isPalindrom(self, s):
        if len(s)%2 == 0:
            right = len(s)//2
            left = right - 1
        else:
            right = len(s)//2 + 1
            left = len(s)//2 - 1
        while left >= 0:
            if s[left] != s[right]:
                return False
            left-=1
            right+=1
        return True