class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefCount = {0:1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num
            count += prefCount.get(prefix-k, 0)
            prefCount[prefix] = 1 + prefCount.get(prefix, 0)

        return count