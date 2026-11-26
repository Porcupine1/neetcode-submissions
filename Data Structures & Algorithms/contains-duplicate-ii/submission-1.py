from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        n = len(nums)
        seen = set()
        for r in range(n):
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            if r-l == k:
                seen.remove(nums[l])
                l += 1

        return False