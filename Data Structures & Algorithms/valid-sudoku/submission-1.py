class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            for j in range(n):
                
                curr = board[i][j]

                if curr == '.': continue
                
                for x in range(n):
                    if x == i:
                        continue
                    if board[x][j] == curr:
                        return False
                
                for y in range(n):
                    if y == j:
                        continue
                    if board[i][y] == curr:
                        return False
                
                start_row = (i//3)*3
                start_col = (j//3)*3

                for x in range(start_row, start_row+3):
                    for y in range(start_col, start_col+3):
                        if x == i and y == j:
                            continue
                        if board[x][y] == curr:
                            return False
        return True