class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i, e in enumerate(nums):
            other = target - e
            if other in hashset:
                return [hashset[other], i]
            else:
                hashset[e] = i