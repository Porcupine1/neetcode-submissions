class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        curr = prices[0]

        for num in prices:
            best = max(best, num - curr)
            curr = min(curr, num)

        return best