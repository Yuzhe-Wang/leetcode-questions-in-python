class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # reverse the inputs for convience
        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        # multiplication
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                result[i + j] += digit
                result[i + j + 1] += result[i+j]// 10
                result[i+j] = result[i+j]%10 
         
        # reverse the result back to normal order
        result = result[::-1]
        temp = 0
        
        # eliminate leading zeros
        while temp < len(result) and result[temp] == 0:
            temp += 1
            
        # convert the result back to a string
        result = map(str, result[temp:])
        return "".join(result)