class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        result = []
        while left <= right and top <= bottom:
            # output the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            if top > bottom: break
    
            # output the right column
            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1
            if left > right: break
                
            # output the bottom row
            for k in range(right, left-1, -1):
                result.append(matrix[bottom][k])
            bottom -= 1
            if top > bottom: break
                
            # output the left column
            for q in range(bottom, top-1, -1):
                result.append(matrix[q][left])
            left += 1
            if left > right: break
            
        return result