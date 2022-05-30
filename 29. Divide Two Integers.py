class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) ^ (divisor < 0)
        dd = abs(dividend)
        dr = abs(divisor)
        res = 0
        while dd >= dr:
            temp = dr
            mul = 1
            while dd >= (temp << 1):
                temp <<= 1
                mul <<= 1
            res += mul
            dd -= temp
        if negative:
            res *= -1
        if res > 2**31-1:
            return 2**31-1
        elif res < -2**31:
            return -2**31
        else:
            return res