from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = defaultdict(int)
        for num in nums:
            maps[num] += 1
            if maps[num] > 1:
                return True
        return False