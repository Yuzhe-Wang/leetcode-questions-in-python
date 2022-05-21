class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            res = max(res, w*h)
            if(height[left] > height[right]):
                right -= 1
            else:
                left += 1
        return res