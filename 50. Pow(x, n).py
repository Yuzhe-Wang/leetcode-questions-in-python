class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if x == 0: return 0
        if n < 0:
            negative = True
        result = self.helper(x,abs(n))
        if negative:
            result = 1/result
        return result
    
    def helper(self, x, n):
        # base cases:
        if n == 0:
            return 1
        
        # recurrsive step
        half = self.helper(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x