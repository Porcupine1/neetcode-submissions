class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len (t)
        dp = [[None for _ in range(n)] for _ in range(m)]
        def dfs(i, j, curr):
            if i==m:
                return curr+n-j == 1
            if j == n:
                return curr+m-i == 1

            if dp[i][j]:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = dfs(i+1, j+1, curr)
            else:
                dp[i][j] = dfs(i+1, j+1, curr+1) or dfs(i, j+1, curr+1) or dfs(i+1, j, curr+1)

            return dp[i][j]

        return dfs(0, 0, 0)