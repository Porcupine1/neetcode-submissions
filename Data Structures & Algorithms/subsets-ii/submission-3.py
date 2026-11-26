class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def find_sub(curr, ind):
            res.append(curr[:])
            
            for j in range(ind, len(nums)):
                if j> ind and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                find_sub(curr, j+1)
                curr.pop()


        find_sub([], 0)
        return res