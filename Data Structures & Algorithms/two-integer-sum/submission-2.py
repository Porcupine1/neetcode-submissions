class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ints_map = {}

        for i, e in enumerate(nums):
            if target - e in ints_map:
                return [ints_map[target - e], i]
            ints_map[e] = i