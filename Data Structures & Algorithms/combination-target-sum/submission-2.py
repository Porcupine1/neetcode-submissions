class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def find_combo(curr, ind, rem):
            if rem == 0:
                res.append(curr[:])
                return

            for j in range(ind, len(nums)):
                if rem-nums[j] < 0:
                    return
                curr.append(nums[j])
                find_combo(curr, j, rem-nums[j])
                curr.pop()

        find_combo([], 0, target)
        return res