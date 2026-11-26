from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefCount = defaultdict(int)
        prefCount[0] += 1
        
        count = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in prefCount:
                count += prefCount[prefix - k]

            prefCount[prefix] += 1

        return count