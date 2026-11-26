class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[(nums[i]%n)-1] // n > 0:
                return nums[i]%n
            nums[(nums[i]%n)-1] += n