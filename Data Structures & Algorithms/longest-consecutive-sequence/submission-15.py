class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        best = 0

        for i in range(len(nums)):
            if nums[i]-1 not in lookup:
                curr = nums[i]
                while curr in lookup:
                    curr += 1
                best = max(curr - nums[i], best)
        return best