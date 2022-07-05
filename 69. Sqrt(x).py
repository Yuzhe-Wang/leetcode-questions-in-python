class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left)//2
            print(mid)
            temp = mid * mid
            if temp == x:
                return mid
            elif temp < x and (mid+1)*(mid+1) > x:
                return mid
            elif temp > x:
                right = mid - 1
            else:
                left = mid + 1
        return -1