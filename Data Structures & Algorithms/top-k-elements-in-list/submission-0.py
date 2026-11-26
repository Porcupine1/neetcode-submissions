from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for x in range(len(nums)+1)]
        count = defaultdict(int)

        for num in nums:
            if count[num] >= 1:
                freq[count[num]].remove(num)
            count[num] += 1
            freq[count[num]].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
                

        