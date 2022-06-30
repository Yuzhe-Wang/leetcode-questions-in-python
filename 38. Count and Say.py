class Solution:
    def countAndSay(self, n: int) -> str:
        return self.helper(n) 
    
    def helper(self, n:int) -> str:
        # base case:
        if n == 1:
            return "1"
        
        # recurrsive step:
        temp = self.countAndSay(n-1)
        result = ""
        l = 0
        r = 0
        while l < len(temp) and r < len(temp):
            while temp[r] == temp[l]:
                r += 1
                if r >= len(temp): break
            result += str(r - l)
            result += temp[l]
            l = r
        return result