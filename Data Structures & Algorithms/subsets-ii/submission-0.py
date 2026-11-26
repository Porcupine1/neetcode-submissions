class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def find_subsets(curr, i):
            if i == len(nums):
                res.append(curr[:])
                return
            
            
            curr.append(nums[i])
            find_subsets(curr, i+1)
            curr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            find_subsets(curr, i+1)

        find_subsets([], 0)
        return res