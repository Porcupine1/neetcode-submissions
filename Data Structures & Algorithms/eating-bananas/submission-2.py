class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            k = l + (r - l) // 2
            time = sum([math.ceil(x/k) for x in piles])
            if h < time:
                l = k + 1
            elif time <= h:
                r = k

        return l