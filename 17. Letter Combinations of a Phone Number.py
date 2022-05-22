class Solution:
    dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        
        self.helper(digits, 0, "",res)
        return res
        
    def helper(self, digits, i, temp, res):
        # base case
        if i == len(digits):
            res.append(temp)
            return
        
        # recurrsive step
        digit = digits[i]
        for letter in self.dic[digit]:
            temp += letter
            self.helper(digits, i+1, temp, res)
            temp = temp[0:len(temp)-1]