class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0

        dp = [0 for _ in range(n+2)]
        dp[n-2] = max(0, prices[n-1] - prices[n-2])

        for b in range(n-3, -1, -1):
            for s in range(b+1, n):
                dp[b] = max(dp[b], dp[b+1], prices[s]-prices[b]+dp[s+2])

        return dp[0]
