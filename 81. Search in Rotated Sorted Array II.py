class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            # determine which portion are we in
            if nums[left] == nums[mid]:
                # this gives no info about which portion we are in
                left += 1
            elif nums[left] < nums[mid]:
                # we are in the left portion
                if target > nums[mid]:
                    left = mid + 1
                else:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                # we are in the right portion
                if target < nums[mid]:
                    right = mid - 1
                else:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False