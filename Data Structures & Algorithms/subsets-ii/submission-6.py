class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def findSubs(curr, i):
            res.append(curr[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                findSubs(curr+[nums[j]], j+1)

        findSubs([], 0)
        return res