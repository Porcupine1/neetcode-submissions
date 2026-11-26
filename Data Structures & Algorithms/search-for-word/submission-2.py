class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])
        
        def search(r, c, i):
            if i == len(word):
                return True
            if min(r, c) < 0 or r >= h or c >= w or word[i] != board[r][c]:
                return False
            
            
            board[r][c] = "#"
            i +=1
            res = search(r+1, c, i) or search(r, c+1, i) or search(r-1, c, i) or search(r, c-1, i)
            board[r][c] = word[i-1]
            return res

        for r in range(h):
            for c in range(w):
                if search(r, c, 0):
                    return True
        return False
