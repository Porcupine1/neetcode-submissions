class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w = len(grid[0])
        h = len(grid)

        def dfs(x, y):
            if min(x,y) < 0 or x >= w or y>=h or grid[y][x] == "0":
                return
            
            grid[y][x] = "0"
            dfs(x, y+1) #down
            dfs(x, y-1) #up
            dfs(x-1, y) #left
            dfs(x+1, y) #right

        res = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == "1":
                    dfs(x, y)
                    res += 1

        return res
        