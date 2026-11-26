class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        pref = [nums[0]]
        suff = [nums[-1]]
        res = []
        for i in range(1, len(nums)):
            pref.append(pref[-1]*nums[i])

        for i in range(len(nums)-2, -1, -1):
            print(nums[i]*nums[i+1])
            suff.append(nums[i]*suff[-1])
        suff.reverse()
        print(pref, suff)
        
        res.append(suff[1])
        for i in range(1, len(nums)-1):
            res.append(pref[i-1]*suff[i+1])
        res.append(pref[-2])
        return res
        