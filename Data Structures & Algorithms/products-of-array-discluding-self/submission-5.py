class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]*len(nums)
        suff = [1]*len(nums)

        for i in range(0, n):
            pref[i] = nums[i] if i == 0 else nums[i]*pref[i-1]
        
        for i in range(n-1, -1, -1):
            suff[i] = nums[i] if i == n-1 else nums[i]*suff[i+1]

        res = []
        for i in range(n):
            prod = (1 if i == 0 else pref[i-1]) * (1 if i==n-1 else suff[i+1])
            res.append(prod)
        print(prod)
        
        return res