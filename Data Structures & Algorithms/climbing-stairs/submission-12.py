class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        def dfs(n):
            if n <= 2:
                return n
            if dp[n] != float("inf"):
                return dp[n]
            return dfs(n-1) + dfs(n-2)

        return dfs(n)