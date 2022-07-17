class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # three phases:
        # 1. scan the bouders, change O's into T's
        # 2. scan the grid, change the remaining O's into X's
        # 3. scan the grid again, change the T's into O's
        
        ROW, COL = len(board), len(board[0])
        
        def dfs(r, c):
            # base case
            if c<0 or r<0 or c==COL or r==ROW or board[r][c]!='O':
                return
            
            # recurrsive step
            board[r][c]='T'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            
        for i in range(ROW):
            for j in range(COL):
                if board[i][j]=='O' and (i in [0,ROW-1] or j in [0,COL-1]):
                    dfs(i,j)
                    
        for i in range(ROW):
            for j in range(COL):
                if board[i][j]=='O':
                    board[i][j]='X'
            
        for i in range(ROW):
            for j in range(COL):
                if board[i][j]=='T':
                    board[i][j]='O'