class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        prefCount = {0:1}
        pref = 0

        for num in nums:
            pref += num
            res += prefCount.get(pref-goal, 0)
            prefCount[pref] = 1 + prefCount.get(pref, 0)

        return res