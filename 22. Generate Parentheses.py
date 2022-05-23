class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, 0, 0, "", res)
        return res
    
    def helper(self, n, l, r, temp, res):
        # base case
        if l < r or l > n or r > n:
            return
        # found one valid solution
        if l == r == n:
            res.append(temp)
            return
        
        # recurrsive step
        # check if we can put a closing parenthesses
        if l > r:
            temp += ")"
            self.helper(n, l, r+1, temp, res)
            temp = temp[:-1]
            
        temp += "("
        self.helper(n, l+1, r, temp, res)
        temp = temp[:-1]