class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        one, two = len(word1), len(word2)
        dp = [[float('inf') for _ in range(two)] for _ in range(one)]
        def dfs(i, j):
            if i == one:
                return two-j
            if j == two:
                return one-i

            if dp[i][j]!=float('inf'):
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] =  dfs(i+1, j+1)

            else:
                dp[i][j] = 1+min(dfs(i+1, j+1), dfs(i+1, j), (dfs(i, j+1)))

            return dp[i][j]

        return dfs(0,0)