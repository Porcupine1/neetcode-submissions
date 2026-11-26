class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0

        for num in nums:
            if not num-1 in unique:
                curr = num
                count = 0
                while curr in unique:
                    curr += 1
                    count += 1
                res = max(res, count)

        return res