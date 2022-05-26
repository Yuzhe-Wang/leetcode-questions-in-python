class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        curr = nums[0]
        for i in range(len(nums)):
            if nums[i] == curr:
                continue
            else:
                nums[index] = nums[i]
                curr = nums[index]
                index += 1
        return index