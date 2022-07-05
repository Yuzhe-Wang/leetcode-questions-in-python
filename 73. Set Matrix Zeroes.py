class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [0] * len(matrix)
        col = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
                
        for k in range(len(row)):
            if row[k] == 1:
                for q in range(len(matrix[k])):
                    matrix[k][q] = 0
        
        for m in range(len(col)):
            if col[m] == 1:
                for n in range(len(matrix)):
                    matrix[n][m] = 0
        
        return