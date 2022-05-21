class Solution:
    def isPalindrome(self, x: int) -> bool:
        # # approach1: reverse the entire string
        # val = str(x)
        # rev = val[::-1]
        # if val == rev:
        #     return True
        # else:
        #     return False
        
        # approach2: reverse half of the num and compare
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10
        if x == reverse or x == reverse // 10:
            return True
        else:
            return False