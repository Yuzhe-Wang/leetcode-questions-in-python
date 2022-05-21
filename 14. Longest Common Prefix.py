class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        res = ""
        for i in range(len(word)):
            pref = word[0:i+1]
            common = True
            for str in strs:
                if i >= len(str) or str[0:i+1] != pref:
                    common = False
                    break
            if common:
                res = pref
            else:
                break
        return res