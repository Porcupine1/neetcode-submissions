class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                i
                seen.add(val)

        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                val = board[j][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                val = board[j][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for k in range(9):
                    r = k//3 + i
                    c = k%3 + j
                    val  = board[r][c]
                    if val == ".":
                        continue
                    if val in seen:
                        return False
                    seen.add(val)

        return True
        
