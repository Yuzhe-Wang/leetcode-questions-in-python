class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        
        for i,a in enumerate(haystack):
            if a != needle[0]:
                continue
            else:
                temp = i
                j = 0
                while temp < len(haystack) and j < len(needle):
                    if haystack[temp] == needle[j]:
                        temp += 1
                        j += 1
                    else:
                        break
                if j==len(needle):
                    return i
        return -1 