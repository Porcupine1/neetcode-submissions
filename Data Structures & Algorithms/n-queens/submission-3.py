class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posD = set()
        negD = set()
        
        def solve(curr, r):
            if r == n:
                res.append(curr[:])

            for c in range(n):
                if c in col or (r-c) in negD or (r+c) in posD:
                    continue
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                curr.append(("."*(c))+"Q"+("."*(n-c-1)))
                
                solve(curr, r+1)
                
                curr.pop()
                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)

        state = [[0 for _ in range(n)] for _ in range(n)]
        solve([], 0)
        return res
        