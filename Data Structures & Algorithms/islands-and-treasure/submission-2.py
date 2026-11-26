class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647
        neigh = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        gates = []

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    gates.append((i, j))

        level = 1
        while gates:
            layer = []
            for x, y in gates:
                for dx, dy in neigh:
                    newX, newY = x+dx, y+dy
                    if min(newX, newY) < 0 or newX >= ROW or newY >= COL:
                        continue
                    if grid[newX][newY] == INF:
                        grid[newX][newY] = level
                        layer.append((newX, newY))
            gates = layer
            level += 1