class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = [[0]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, 0, word, used):
                    return True
        return False
    
    def dfs(self, board, i, j, curr, word, used):
        # base cases:
        if curr == len(word)-1 and board[i][j] == word[curr]:
            return True
        if board[i][j] != word[curr]:
            return False
         
        # recurrsive step
        used[i][j] = 1
        result = False
        if i-1 > -1 and used[i-1][j] != 1:
            if self.dfs(board, i-1, j, curr+1, word, used):
                result = True
                
        if j-1 > -1 and used[i][j-1] != 1:
            if self.dfs(board, i, j-1, curr+1, word, used):
                result = True
                
        if i+1 < len(board) and used[i+1][j] != 1:
            if self.dfs(board, i+1, j, curr+1, word, used):
                result = True
                
        if j+1 < len(board[0]) and used[i][j+1] != 1:
            if self.dfs(board, i, j+1, curr+1, word, used):
                result = True
        used[i][j] = 0
        return result