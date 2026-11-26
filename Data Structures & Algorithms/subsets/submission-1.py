class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def find_sub(curr, ind):
            res.append(curr[:])

            for j in range(ind, len(nums)):
                curr.append(nums[j])
                find_sub(curr, j+1)
                curr.pop()

        find_sub([], 0)

        return res