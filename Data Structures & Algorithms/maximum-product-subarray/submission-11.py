class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        gmin = 1
        gmax = 1
        res = float("-inf")

        for num in nums:
            temp = gmax
            gmax = max(gmax*num, gmin*num, num)
            print(gmax)
            gmin = min(temp*num, gmin*num, num)
            res = max(gmax, res)

        return res
