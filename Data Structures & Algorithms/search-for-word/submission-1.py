class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])

        def find_word(row, col, ind):
            if ind == len(word):
                return True
            if (min(row, col) < 0 or row >= ROW or col >= COL or board[row][col] != word[ind] or board[row][col] == "#"):
                return False
            
            board[row][col] = "#"
            dirs = [(row+i, col+j) for i in range(-1, 2) for j in range(-1, 2) if abs(i) != abs(j)]
            res = [find_word(r, c, ind+1) for r, c in dirs]
            board[row][col] = word[ind]
            return any(res)

        for i in range(ROW):
            for j in range(COL):
                if find_word(i, j, 0):
                    return True
        return False

