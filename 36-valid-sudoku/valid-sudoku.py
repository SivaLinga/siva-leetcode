from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # key = row_number
        cols = defaultdict(set) # key = col_number
        squares = defaultdict(set) # key = (row_number, col_number)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if (cell in rows[row] or cell in cols[col] or cell in squares[(row // 3, col // 3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True

