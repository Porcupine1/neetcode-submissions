class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        

        for i in range(1, n+1):
            j = i
            for cost, dur in zip(costs, [1,7,30]):
                while j > 0 and days[i-1]-dur < days[j-1]:
                    j -= 1
                dp[i] = min(dp[i], cost+dp[j])
        return dp[n]