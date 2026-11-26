from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        neigh = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0
        freshCount = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    freshCount += 1

        while q:
            x, y, time = q.popleft()

            for dx, dy in neigh:
                newX, newY = x+dx, y+dy

                if min(newX, newY) < 0 or newX >= ROW or newY >= COL or grid[newX][newY] != 1:
                    continue
                
                grid[newX][newY] = 2
                freshCount -= 1
                q.append((newX, newY, time+1))
                res = time+1
                


        return res if freshCount == 0 else -1

