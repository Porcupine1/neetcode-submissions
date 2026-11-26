from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        hm = defaultdict(set)

        res = []
        for num in nums:
            hm[counter[num]].add(num)
        
        for i in range(len(nums), 0, -1):
            res.extend(hm[i])
            if len(res) >= k:
                break
        return res[:k+1]