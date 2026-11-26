class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set()
        negDiag = set()
        cols  = set()
        res = []
        board = [["."]*n for _ in range(n)]

        def find(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                if col in cols or (row-col) in negDiag or (row+col) in posDiag:
                    continue
                cols.add(col)
                negDiag.add(row-col)
                posDiag.add(row+col)
                board[row][col] = "Q"

                find(row+1)

                board[row][col] = "."
                cols.remove(col)
                negDiag.remove(row-col)
                posDiag.remove(row+col)


        find(0)
        return res
