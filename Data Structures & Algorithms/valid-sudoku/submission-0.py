class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for row in range(n):
            for col in range(n):
                if board[row][col] != ".":
                    num = board[row][col]

                    for i in range(n):
                        if not i == row and board[i][col] == num:
                            return False
                    
                    for j in range(n):
                        if not j == col and board[row][j] == num:
                            return False

                    start_row = (row//3)*3
                    start_col = (col//3)*3
                    for i in range(start_row, start_row+3):
                        for j in range(start_col, start_col+3):

                            if not i == row and not j == col and board[i][j] == num:
                                return False

        return True

                    