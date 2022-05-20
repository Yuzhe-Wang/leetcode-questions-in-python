class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # regular sliding window O(2n)
        '''
        dic = {}
        left = right = 0
        result = 0
        
        while left <= right and right < len(s):
            letter = s[right]
            if letter not in dic or dic[letter] == 0:
                dic[letter] = 1
                result = max(result, right - left + 1)
                right += 1
            else:
                dic[s[left]] -= 1
                left += 1
        
        return result
        '''
        
        # optimized sliding window, O(n)
        result = 0
        dic = {}
        i = 0
        for j in range(len(s)):
            letter = s[j]
            if letter in dic:
                i = max(dic[letter], i)
            result = max(result, j - i + 1)
            # update the index to the next of the current letter
            dic[letter] = j + 1
        return result  