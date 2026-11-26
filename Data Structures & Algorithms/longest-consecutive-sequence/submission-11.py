class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        maxCount = 0

        for num in mp:
            if num - 1 not in mp:
                currCount = 1
                while num + currCount in mp:
                    currCount += 1
                maxCount = max(maxCount, currCount)
        
        return maxCount