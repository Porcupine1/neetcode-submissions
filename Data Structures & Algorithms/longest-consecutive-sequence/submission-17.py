class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_hp = set(nums)

        for num in nums_hp:
            if num - 1 not in nums_hp:
                curr  = num
                count = 0
                while curr in nums_hp:
                    count += 1
                    curr += 1
                res = max(res, count)

        return res