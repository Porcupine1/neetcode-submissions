class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(n):
            if n <= 1:
                return 0
            return min(dfs(n-1)+cost[n-1], dfs(n-2)+cost[n-2])

        return dfs(len(cost))