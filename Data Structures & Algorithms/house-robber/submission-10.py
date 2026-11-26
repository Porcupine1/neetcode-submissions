class Solution:
    def rob(self, nums: List[int]) -> int:
        fst, snd = 0, 0
        for num in nums:
            fst, snd = snd, max(fst+num, snd)
        return snd