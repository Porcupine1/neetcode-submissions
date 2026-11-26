class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find_combo(res, nums, curr, i):
            if sum(curr) == target:
                res.append(curr[:])
                return
            
            if i == len(nums) or sum(curr) > target:
                return

            curr.append(nums[i])
            find_combo(res, nums, curr, i)
            curr.pop()
            find_combo(res, nums, curr, i+1)

        res = []
        find_combo(res, nums, [], 0)
        return res