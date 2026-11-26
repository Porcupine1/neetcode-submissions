class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i+1
            k = length - 1

            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and j < length and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and k > 0 and nums[k] == nums[k+1]:
                        k -= 1
                elif currSum < 0:
                    j += 1
                else:
                    k -= 1
        
        return res