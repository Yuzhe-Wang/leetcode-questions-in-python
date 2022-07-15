class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        curr = []
        
        for i in range(1, rowIndex+2):
            for j in range(i):
                if j == 0 or j == i-1:
                    curr.append(1)
                else:
                    curr.append(result[-1][j-1]+result[-1][j])
            result.append(curr.copy())
            curr = []
        return result[-1]