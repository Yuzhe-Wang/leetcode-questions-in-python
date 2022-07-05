class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''idea: use two binary searches, the first one is to find the correct row
            and the second one is to find the actual element inside the row'''
        top = 0
        bottom = len(matrix) - 1
        targetRow = -1
        
        # find the correct row
        while top <= bottom:
            mid = (top + bottom)//2
            low = matrix[mid][0]
            high = matrix[mid][len(matrix[0]) - 1]
            if low <= target and high >= target:
                targetRow = mid
                break
            elif target < low:
                bottom = mid - 1
            else:
                top = mid + 1
        
        # find the actual number
        if targetRow == -1:
            return False
        else:
            left = 0
            right = len(matrix[targetRow]) - 1
            while left <= right:
                m = (left + right)//2
                curr = matrix[targetRow][m]
                if curr == target:
                    return True
                elif curr < target:
                    left = m + 1
                else:
                    right = m - 1
            return False