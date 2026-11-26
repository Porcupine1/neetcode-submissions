class Solution:
    def climbStairs(self, n: int) -> int:
        fst = 1
        snd=2
        if n == 1:
            return 1
        if n==2:
            return 2
        
        for _ in range(n-2):
            fst, snd = snd, fst+snd
        return snd

        