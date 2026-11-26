class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        fst, snd = cost[0], cost[1]

        for i in range(2, len(cost)):
            print(fst,snd)
            fst, snd = snd, min(fst, snd)+cost[i]
            print(fst,snd)
        return min(fst, snd)