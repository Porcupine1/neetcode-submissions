class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = 1
        minP = 1
        res = float('-inf')

        for num in nums:
            temp = maxP
            maxP = max([num, maxP*num, minP*num])
            minP = min([num, temp*num, minP*num])
            res = max(res, maxP)
        
        return res
