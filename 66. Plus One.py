class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [0] * len(digits)
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + carry
            result[i] = sum % 10
            carry = sum // 10
        if carry != 0:
            result = [carry] + result
        return result