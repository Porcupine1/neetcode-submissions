class Solution:
    def helper(self, nums):
        a, b = 0, 0

        for i in range(len(nums)):
            a, b = b, max(b, a+nums[i])
        return b

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums)-1]))