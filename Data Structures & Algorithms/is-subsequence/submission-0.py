class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]

        def dfs(i, j):
            if i == m:
                return True
            if j == n:
                return False

            if dp[i][j]:
                return dp[i][j]

            dp[i][j] = dfs(i,j+1)
            if s[i] == t[j]:
                dp[i][j] = dp[i][j] or dfs(i+1, j+1)

            return dp[i][j]

        return dfs(0, 0)
            