class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n  = len(grid), len(grid[0])
        if grid[0][0]==1:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for r in range(m):
            if grid[r][0]==0:
                dp[r][0] = 1
            else:
                break
        for c in range(n):
            if grid[0][c]==0:
                dp[0][c] = 1
            else:
                break

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if grid[i][j]==0 else 0

        return dp[m-1][n-1]