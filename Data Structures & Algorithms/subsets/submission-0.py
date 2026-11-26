class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def generate_subsets(res, i, curr):
            if i == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            generate_subsets(res, i+1, curr)
            curr.pop()
            generate_subsets(res, i+1, curr)
                
        generate_subsets(res, 0, [])
        return res