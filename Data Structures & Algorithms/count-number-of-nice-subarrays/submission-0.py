from collections import deque

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = deque()
        res = 0
        l = 0

        for r in range(len(nums)):
            if nums[r]%2==1:
                odds.append(r)
            if len(odds) > k:
                new = odds.popleft()
                l = new+1
            if len(odds) == k:
                res += odds[0] - l + 1
        
        return res
            
            
