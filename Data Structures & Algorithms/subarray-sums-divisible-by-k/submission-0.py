class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remCount = {0:1}
        res = 0
        pref = 0

        for num in nums:
            pref += num
            rem = pref%k
            res += remCount.get(rem, 0)
            remCount[rem] = 1+ remCount.get(rem, 0)

        return res