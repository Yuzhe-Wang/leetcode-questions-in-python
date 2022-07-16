class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0
        for num in nums:
            if num-1 not in numSet:
                temp = 0
                while (num+temp) in numSet:
                    temp += 1
                result = max(result, temp)
        return result