class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            want_num = target - num
            if want_num in seen:
                return [seen[want_num], idx]
            seen[num] = idx