class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l=r=0
        res = 0

        while r<n:
            prof = prices[r] - prices[l]
            
            if prof < 0:
                l=r

            res = max(res, prof)
            r+=1
        
        return res