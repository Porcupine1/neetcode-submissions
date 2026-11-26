class Solution:
    def climbStairs(self, n: int) -> int:
        fst = snd = 1

        for _ in range(n):
            fst, snd = snd, snd + fst

        return fst