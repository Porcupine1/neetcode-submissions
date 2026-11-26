class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = set(nums)
        counts = {}


        for num in unique:
            curr = num
            count = 1
            
            while curr-1 in unique:
                curr -= 1
                if curr in counts:
                    count += counts[curr]
                    break
                count += 1
            
            counts[num] = count
        return max(counts.values())