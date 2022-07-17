class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        total = 0
        for i in range(32):
            total = 0
            for num in nums:
                total += (num>>i)&1
            result |= (total%3)<<i
        # because python uses sign-magnitude internal format, eliminate the negative sign when the result is negative
        if(result >> 31 & 1) == 1: result -= 1 <<32
        return result