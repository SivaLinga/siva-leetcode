class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #condition1:
        for row_index, row in enumerate(board):
            row_map = {}
            for cell in row:
                if cell == ".": continue
                if cell in row_map:
                    return False
                else:
                    row_map[cell] = 1

        # condition2:
        for y in range(9):
            column_map = {}
            for x in range(9):
                if board[x][y] == ".": continue
                if board[x][y] in column_map:
                    return False
                else:
                    column_map[board[x][y]] = 1
        # condition 3:
        x1 = 0
        y1 = 0


        while(x1 < 9 or y1 < 9):
            sub_grid_map = {}
            for x2 in range(x1, x1+3):
                for y2 in range(y1, y1+3):
                    print(x2,y2)
                    if board[x2][y2] == ".": continue
                    if board[x2][y2] in sub_grid_map:
                        return False
                    else:
                        sub_grid_map[board[x2][y2]] = 1
            if x2 == 8 and y2 == 8:
                break
            elif y2 == 8:
                y1 = 0
                x1 = x1 + 3
            else:
                y1 = y1 + 3
        return True
