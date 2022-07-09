# a longer solution
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        curr = []
        dots = 3
        self.dfs(s, dots, curr, result)
        return result
        
    def dfs(self, s, dots, curr, result):
        # base case: no more dots available
        if dots == 0:
            if len(s)>0 and self.isValid(s):
                temp = ".".join(curr)
                temp += "." + s
                result.append(temp)
                return
        
        # recurrsive step: try all possible positions for the current dot
        for i in range(1, len(s)+1):
            temp = s[:i]
            if self.isValid(temp):
                curr.append(temp)
                rest = s[i:]
                self.dfs(rest, dots-1, curr, result)
                curr.pop()
            else:
                break
        
    def isValid(self,s):
        if len(s) >3:
            return False
        if not int(s) in range(0,256):
            return False
        if s[0] == '0' and len(s) > 1:
            return False
        return True

# a shorter solution
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def dfs(index, dots, curr):
            # base case:
            if dots == 0 and index == len(s):
                # remove the last dot
                result.append(curr[:-1])
            
            # recurrsive step
            for i in range(index, len(s)):
                if int(s[index:i+1]) < 256 and (i==index or s[index] != '0'):
                    dfs(i+1, dots-1, curr+s[index:i+1]+'.')
                else:
                    break
        
        dfs(0, 4, "")
        return result