import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        sqrt_len = int(math.sqrt(rows))

        rows_set = [set() for i in range(rows)]
        cols_set = [set() for j in range(cols)]
        squares_set = [set() for k in range(cols)]

        for row in range(rows):
            for col in range(cols):
                print(col)
                num = board[row][col]
                if num == '.':
                    continue
                sq_index = (row//sqrt_len) * sqrt_len + (col//sqrt_len)
                if num in rows_set[row] or num in cols_set[col] or num in squares_set[sq_index]:
                    return False
                rows_set[row].add(num)
                cols_set[col].add(num)
                squares_set[sq_index].add(num)

        return True