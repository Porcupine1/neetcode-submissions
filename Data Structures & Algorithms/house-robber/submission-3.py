class Solution:
    def solve(self, i, nums, T):
        if i >= len(nums):
            return T[0]
        if T[i] == float("-infinity"):
            T[i] = max(self.solve(i-1, nums, T), nums[i]+self.solve(i-2, nums, T))
        return T[i]
    def rob(self, nums: List[int]) -> int:
        T = [float("-infinity")]*(len(nums)+2)
        T[0] = nums[0]
        if len(nums) >= 2:
            T[1] = max(nums[0], nums[1])
        
        return self.solve(len(nums)-1, nums, T)