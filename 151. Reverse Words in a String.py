class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        left = right = 0
        while right < len(s):
            if s[right] != " ":
                left = right
                while right < len(s) and s[right] != " ":
                    right += 1
                stack.append(s[left:right])
            right += 1
        
        result = ""
        while stack:
            result += stack.pop() 
            if stack:
                result += " "
        return result