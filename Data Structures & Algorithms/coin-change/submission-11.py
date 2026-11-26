class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {}
        def dfs(amount):
            if amount < 0:
                return float('inf')
            
            if amount == 0:
                return 0

            if dp and amount in dp:
                return dp[amount]

            dp[amount] = min([1+dfs(amount-coin) for coin in coins])

            return dp[amount]
        res = dfs(amount) 
        return res if res!=float('inf') else -1