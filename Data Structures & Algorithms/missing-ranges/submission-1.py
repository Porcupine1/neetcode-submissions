class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[lower, upper]]
        res = []
        for i in range(n+1):
            if i == 0:
                if  nums[0] != lower:
                    res.append([lower, nums[0]-1])
                continue
            if i == n:
                if  upper != nums[n-1]:
                    res.append([nums[n-1]+1, upper])
                continue

            if nums[i] != nums[i-1]+1:
                res.append([nums[i-1]+1, nums[i]-1])

        return res
            