class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def getSubsets(curr, i):
            if i >= len(nums):
                res.append(curr[:])
                return
            getSubsets(curr + [nums[i]], i+1)
            getSubsets(curr, i+1)

        getSubsets([], 0)
        return res
