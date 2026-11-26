class Solution:
    def climbStairs(self, n: int) -> int:
        fst = snd = 1

        for _ in range(n-1):
            fst, snd = snd, fst+snd

        return snd