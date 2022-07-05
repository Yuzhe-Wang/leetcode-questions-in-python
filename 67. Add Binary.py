class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        length = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        carry = 0
        for i in range(length):
            x = 0
            if i < len(a):
                x = int(a[i])
            y = 0
            if i < len(b):
                y = int(b[i])
            digit = x ^ y ^ carry
            carry = (x & y) or (x & carry) or (y & carry)
            result += str(digit)
        if carry != 0:
            result += str(carry)
        result = result [::-1]
        return result