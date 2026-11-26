class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def findCombo(curr, i):
            res.append(curr[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                findCombo(curr, j+1)
                curr.pop()

        findCombo([], 0)
        return res