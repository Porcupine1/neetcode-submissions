class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l=r=0
        res = 0

        while l<n:
            prof = prices[r] - prices[l]
            if r==n-1:
                res = max(res, prof)
                l+=1
                continue
            
            if prof < 0:
                l=r

            res = max(res, prof)
            
            if r < n-1:
                r+=1
        
        return res