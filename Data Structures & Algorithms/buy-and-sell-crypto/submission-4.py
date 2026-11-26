class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r=0,1
        best = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            best = max(best, profit)
            if profit < 0:
                l = r
            else:
                r+=1
        return best
