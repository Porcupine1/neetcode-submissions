class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def findPerms(nums, i):
            if i == len(nums):
                res.append(nums[:])
                return nums
            print(nums)
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                findPerms(nums, i+1)
                nums[i], nums[j] = nums[j], nums[i]

        findPerms(nums, 0)
        return res