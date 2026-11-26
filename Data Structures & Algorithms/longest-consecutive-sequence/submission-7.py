class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        l = 0

        if len(nums) == 0:
            curr_res = 0
            max_res = 0
        else:
            curr_res = 1
            max_res = 1

        for r in range(1, len(nums)):
            if abs(nums[r] - nums[r-1]) > 1:
                curr_res = 1
                continue
            if abs(nums[r] - nums[r-1]) == 1:
                curr_res += 1
            max_res = max(curr_res, max_res)

        return max_res