class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def findCombo(arr, zero, i):
            if zero == 0:
                res.append(arr[:])

            for j in range(i, len(nums)):
                val = nums[j]
                if zero - val < 0:
                    return
                findCombo(arr + [val], zero-val, j)

        findCombo([], target, 0)
        return res
