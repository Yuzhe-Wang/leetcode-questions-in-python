class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                b = nums[j]
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, len(nums) - 1
                temp = target - a - b
                while l < r:
                    c, d = nums[l], nums[r]
                    if c+d < temp:
                        l += 1
                    elif c+d > temp:
                        r -= 1
                    else:
                        res.append([a,b,c,d])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
        return res