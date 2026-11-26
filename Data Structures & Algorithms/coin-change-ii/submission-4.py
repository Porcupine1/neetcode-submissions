class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for t in range(1, amount+1):
                if t - coins[i-1] >=0:
                    dp[i][t] = dp[i][t-coins[i-1]]
                dp[i][t] += dp[i-1][t]

        return dp[n][amount]