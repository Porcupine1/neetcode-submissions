class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)

        
        maxCount = 0
        for num in nums:
            currCount = 0
            if num - 1 not in mp:
                currCount += 1
                nextNum = num + 1

                while nextNum in mp:
                    currCount += 1
                    nextNum += 1
            maxCount = max(maxCount, currCount)
        
        return maxCount