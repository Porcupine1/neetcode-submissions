from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647
        neigh = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        gates = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    gates.append((i, j, 0))

        while gates:
            x, y, dist = gates.popleft()
            print(x, y)
            for dx, dy in neigh:
                newX, newY = x+dx, y+dy
                if min(newX, newY) < 0 or newX >= ROW or newY >= COL:
                    continue
                if grid[newX][newY] == INF:
                    grid[newX][newY] = dist + 1
                    gates.append((newX, newY, dist+1))