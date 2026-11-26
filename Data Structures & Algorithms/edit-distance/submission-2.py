class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if i == m:
                return n-j
            if j == n:
                return m-i

            if dp[i][j] != float('inf'):
                return dp[i][j]

            # replace with needed char -> doesn't count
            # deleting, progressing i by 1 but j remains contant
            # inserting leaves i constant but progresses j by one
            
            dp[i][j] = 1+min(dfs(i+1, j+1), dfs(i+1, j), dfs(i, j+1))
            
            if word1[i] == word2[j]:
                dp[i][j] = min(dp[i][j],dfs(i+1, j+1))

            return dp[i][j]
        res = dfs(0, 0)
        print(dp)
        return res