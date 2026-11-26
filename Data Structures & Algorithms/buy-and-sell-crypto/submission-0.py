class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r =0, 1
        maxPrice = 0
        while r < len(prices):
            price = prices[r] - prices[l]
            maxPrice = max(maxPrice, price)
            print(price)
            if price < 0:
                l = r
            r+=1

        return maxPrice
