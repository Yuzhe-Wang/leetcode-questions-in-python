class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            a = self.helper(s, i, i)
            b = self.helper(s, i-1, i)
            result = (a if len(a)>len(result) else result)
            result = (b if len(b)>len(result) else result)
        return result
    
    
    def helper(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]