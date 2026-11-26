class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        ROW = len(board)
        COL = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(r, c, word, curr):
            if min(r, c) < 0 or r >= ROW or c >= COL or board[r][c] == "#" or board[r][c] not in curr.children:
                return

            tmp = board[r][c]
            board[r][c] = "#"
            curr = curr.children[tmp]
            word.append(tmp)

            if curr.end:
                res.add("".join(word))
            
            for dr, dc in [(1,0), (0,1), (-1, 0), (0, -1)]:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, word, curr)

            word.pop()
            board[r][c] = tmp

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, [], trie)

        return list(res)
        