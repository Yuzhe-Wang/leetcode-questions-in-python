class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = round(left + (right - left)/2)
            
            if nums[mid] == target:
                return mid
            
            # check which portion of the array mid is at
            # left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
            # right sorted portion
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1 