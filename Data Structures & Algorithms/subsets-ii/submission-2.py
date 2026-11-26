class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        start = prev = 0
        for i in range(len(nums)):
            start = prev if i > 0 and nums[i] == nums[i-1] else 0
            prev = len(res)

            for j in range(start, prev):
                sub = res[j][:]
                sub.append(nums[i])
                res.append(sub)

        return res