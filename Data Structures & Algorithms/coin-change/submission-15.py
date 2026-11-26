class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {}
        def dfs(curr):
            if curr == 0:
                return 0

            if curr < 0:
                return float('inf')
            
            if dp and curr in dp:
                return dp[curr]

            dp[curr] = min(1+dfs(curr-coin) for coin in coins)

            return dp[curr]

        res = dfs(amount)
        return res if res != float('inf') else -1