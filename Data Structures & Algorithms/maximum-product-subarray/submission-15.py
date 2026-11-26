class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        high = 1
        low = 1
        res = float("-inf")

        for num in nums:
            temp = high
            high = max(num, high*num,low*num)
            low = min(num, temp*num, low*num)
            res = max(high, res)

        return res