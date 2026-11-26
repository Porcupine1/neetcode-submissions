from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        atl, pac = set(), set()
        neigh = [(1,0), (-1,0), (0,1), (0, -1)]

        def bfs(q, visit):
            while q:
                r, c = q.popleft()
                visit.add((r,c))

                for dr, dc in neigh:
                    newR, newC = r+dr, c+dc
                    if (min(newR,newC) < 0
                        or newR == ROW
                        or newC == COL
                        or (newR,newC) in visit
                        or heights[r][c] > heights[newR][newC]):

                            continue
                    q.append((newR,newC))
                    

        qa = deque() # pacific queue
        qp = deque() # atlantic queue
        
        
        for c in range(COL):
            qp.append((0, c))
            qa.append((ROW-1, c))

        for r in range(ROW):
            qp.append((r, 0))
            qa.append((r, COL-1)) 

        bfs(qa, atl)
        bfs(qp, pac)

        res = []
        for (r,c) in pac:
            if (r,c) in atl:
                res.append([r,c])
        
        return res
                