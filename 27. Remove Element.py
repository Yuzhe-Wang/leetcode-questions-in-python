class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # find the first occurance of the target value
        curr = -1
        for i,a in enumerate(nums):
            if a==val:
                curr = i
                break
        if curr == -1:
            # nothing to remove
            return len(nums)
        for i in range(curr,len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
        return curr