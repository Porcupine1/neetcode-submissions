class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[None, None] for _ in range(n)]
        

        def dfs(i, buy):
            if i >= n:
                return 0

            if dp[i][buy]:
                return dp[i][buy]

            if buy:
                dp[i][buy] = max(dfs(i+1, buy), dfs(i+1, not buy)-prices[i])
            else:
                dp[i][buy] = max(dfs(i+1, buy), dfs(i+2, not buy)+prices[i])
            
            return dp[i][buy]

        res = dfs(0, 1)
        print(dp)
        return res