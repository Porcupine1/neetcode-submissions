class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        def dfs(n):
            if n <= 3:
                return n
            if dp[n] != float('inf'):
                return dp[n]

            return dfs(n-2) + dfs(n-1)
        return dfs(n)
            