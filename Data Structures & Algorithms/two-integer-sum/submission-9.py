class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            have = nums[i]
            want = target - have

            if want in seen:
                return [seen[want], i]
            seen[have] = i