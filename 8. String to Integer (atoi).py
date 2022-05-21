class Solution:
    def myAtoi(self, s: str) -> int:
        abs = ""
        isNegative = False
        i = 0
        # ignore the leading spaces
        while i < len(s) and s[i] == " ":
            i += 1
        # determine negative or positive
        if i < len(s) and s[i] == "-":
            isNegative = True
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        # convert char one by one
        while i < len(s) and s[i] >= "0" and s[i] <="9":
            abs += s[i]
            i += 1
        # convert it into a num and add the sign
        if len(abs) == 0:
            return 0
        else:
            res = int(abs)
            if isNegative:
                res *= -1
            # check if the value is out of the integers' bound
            if res > 2**31-1:
                return 2**31-1
            elif res < -2**31:
                return -2**31
            else:
                return res
    
        