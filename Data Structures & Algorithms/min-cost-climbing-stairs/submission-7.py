class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * len(cost)

        def dfs(n):
            if n < 0:
                return 0
            
            if dp[n] != float('inf'):
                return dp[n]
            dp[n] = min(dfs(n-1), dfs(n-2)) + cost[n]
            return min(dp[n], dp[n-1])

        return dfs(len(cost)-1)