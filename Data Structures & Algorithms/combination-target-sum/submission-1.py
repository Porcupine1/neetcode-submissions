class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def find_combo(curr, ind, rem):
            if rem < 0:
                return
            if rem == 0:
                res.append(curr[:])
                return
            if ind >= len(nums):
                return

            curr.append(nums[ind])
            find_combo(curr, ind, rem-nums[ind])
            curr.pop()
            find_combo(curr, ind+1, rem)

        find_combo([], 0, target)
        return res