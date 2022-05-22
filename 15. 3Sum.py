class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            target = 0 - a
            while left < right:
                b = nums[left]
                c = nums[right]
                temp = b + c
                if temp < target:
                    left += 1
                elif temp > target:
                    right -= 1
                else:
                    combo = [a,b,c]
                    res.append(combo)
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
        return res