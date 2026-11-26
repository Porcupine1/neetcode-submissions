class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i):
            if i < 0:
                return float('inf')
            if i == 0:
                return 0
            if i in dp and dp[i]:
                return dp[i]

            dp[i] = 1 + min([dfs(i-c) for c in coins])
            return dp[i]

        res = dfs(amount)
        return -1 if res == float('inf') else res