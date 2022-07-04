class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = top = 0
        right = bottom = n-1
        matrix = [[0]*n for i in range(0, n)]
        curr = 1
        while left <= right and top <= bottom:
            # output the top row
            for i in range(left, right+1):
                matrix[top][i] = curr
                curr += 1
            top += 1
            
            # output the right column
            for j in range(top, bottom+1):
                matrix[j][right] = curr
                curr += 1
            right -= 1
            
            # output the bottom row
            for k in range(right, left-1, -1):
                matrix[bottom][k] = curr
                curr += 1
            bottom -= 1
            
            # output the left column
            for q in range(bottom, top-1, -1):
                matrix[q][left] = curr
                curr += 1
            left += 1
            
        return matrix