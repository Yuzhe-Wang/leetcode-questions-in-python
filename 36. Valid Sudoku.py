class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != ".":
                    if (curr in row[i] or 
                        curr in col[j] or
                        curr in box[(i//3,j//3)]):
                        return False
                    else:
                        row[i].add(curr)
                        col[j].add(curr)
                        box[(i//3,j//3)].add(curr)
        return True