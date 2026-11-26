class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1,0], [-1, 0], [0, 1], [0, -1]]
        h = len(grid)
        w = len(grid[0])

        def dfs(x, y):
            if min(x, y) < 0 or x >= w or y >= h or grid[y][x] == 0:
                return 0
            
            grid[y][x] = 0
            res = 1
            for dx, dy in dirs:
                res += dfs(x+dx, y+dy)
            
            return res
        maxA = float('-inf')
        
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:

                    maxA = max(maxA, dfs(x, y))

        return max(maxA, 0)