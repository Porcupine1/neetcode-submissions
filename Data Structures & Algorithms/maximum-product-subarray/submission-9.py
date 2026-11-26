class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = float("-inf")

        for n in nums:
            temp = currMax*n
            currMax = max(n, temp, currMin*n)
            currMin = min(n, temp, currMin*n)
            res = max(res, currMax)

        return res