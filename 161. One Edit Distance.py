class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        
        if abs(ls-lt) > 1 or s == t:
            return False
        
        for i in range(min(ls,lt)):
            if s[i] != t[i]:
                return s[i+1:]==t[i:] or s[i:]==t[i+1:] or s[i+1:]==t[i+1:]
        return True