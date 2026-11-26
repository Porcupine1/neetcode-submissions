class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        n = len(days)

        def dfs(i):
            if i == n:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = float('inf')
            j=i
            for cost, dur in zip(costs, [1,7,30]):
                while j < n and days[i]+dur > days[j]:
                    j += 1
                
                dp[i] = min(dp[i], cost+dfs(j))

            return dp[i]

        return dfs(0)