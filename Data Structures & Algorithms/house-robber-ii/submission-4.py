class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def solve(nums):
            fst, snd = 0, nums[0]

            for i in range(1, len(nums)):
                fst, snd = snd, max(snd, fst+nums[i])

            return snd
        fst = solve(nums[:-1])
        snd = solve(nums[:0:-1])
        return max(fst, snd)

