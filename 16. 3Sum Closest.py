class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[len(nums) - 1]
        for i,a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                curr = a + b + c
                if curr > target:
                    r -= 1
                else:
                    l += 1
                if abs(curr - target) < abs(res - target):
                    res = curr
        return res