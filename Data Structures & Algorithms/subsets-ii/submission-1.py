class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def find_subsets(curr, i):
            res.append(curr[:])
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                find_subsets(curr, j+1)
                curr.pop()

        find_subsets([], 0)
        return res