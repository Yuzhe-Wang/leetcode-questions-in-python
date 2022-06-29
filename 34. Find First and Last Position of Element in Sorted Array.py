class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
    
    # leftMost means we are looking for the left most target
    # direction == right means we are looking for the right most target
    def binarySearch(self, nums, target, leftMost):
        left = 0
        right = len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else: # nums[mid] == target
                result = mid
                if leftMost:
                    right = mid - 1
                else:
                    left = mid + 1
        return result