class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sorted = curr = 2
        while curr < len(nums):
            if nums[curr] == nums[sorted - 2]:
                curr += 1
            else:
                nums[sorted] = nums[curr]
                curr += 1
                sorted += 1
        return sorted