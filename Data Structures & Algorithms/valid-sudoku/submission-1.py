class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = int(len(board) ** 0.5)

        rows_set = [set() for i in range(n*n)]
        cols_set = [set() for j in range(n*n)]
        squares_set = [set() for k in range(n*n)]

        for row in range(n*n):
            for col in range(n*n):
                print(col)
                num = board[row][col]

                if num == '.':
                    continue

                sq_index = (row // n) * n + (col // n)
                
                if num in rows_set[row] or num in cols_set[col] or num in squares_set[sq_index]:
                    return False
                
                rows_set[row].add(num)
                cols_set[col].add(num)
                squares_set[sq_index].add(num)

        return True