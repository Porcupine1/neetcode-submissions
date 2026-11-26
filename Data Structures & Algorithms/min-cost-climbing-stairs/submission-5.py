class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        best = 0
        fst = cost[0]
        snd = cost[1]
        for i in range(2, len(cost)):
            fst, snd = snd, min(fst, snd)+cost[i]

        return min(fst, snd)