class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # idea: sliding window, but use a map to keep track of the unique characters
        if not s or len(s) == 0:
            return 0
        dic = {}
        left = right = 0
        result = 0
        
        while right < len(s):
            if len(dic) <= 2:
                dic[s[right]] = right
                right += 1
            if len(dic) > 2:
                leftMostChar, leftMost = "", len(s)
                for char, index in dic.items():
                    if index < leftMost:
                        leftMost = index
                        leftMostChar = char
                del dic[leftMostChar]
                left = leftMost + 1
            result = max(result, right - left)
        return result