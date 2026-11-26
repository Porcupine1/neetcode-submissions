class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def findCombo(curr, i):
            if i == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            findCombo(curr, i+1)
            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i +=1
            findCombo(curr, i+1)

        findCombo([], 0)
        return res
            