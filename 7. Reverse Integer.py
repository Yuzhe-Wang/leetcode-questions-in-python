class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        if x < 0:
            num = num[0:1] + num[1:][::-1]
        else:
            num = num[::-1]
        res = int(num)
        if res > 2**31 - 1 or res < -2**31:
            return 0
        else:
            return res