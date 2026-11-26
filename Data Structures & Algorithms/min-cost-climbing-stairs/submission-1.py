class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[-1], 0

        for i in range(len(cost)-2, -1,-1):
            a, b = min(cost[i]+a, cost[i]+b), a
        return min(a,b)