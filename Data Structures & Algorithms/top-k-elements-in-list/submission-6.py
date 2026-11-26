from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = defaultdict(int)
        freqToNum = [[] for i in range(len(nums)+1)]
        for num in nums:
            numToFreq[num] += 1
        
        for num, freq in numToFreq.items():
            freqToNum[freq].append(num)

        count = 0
        res = []
        for i in range(len(freqToNum)-1, 0, -1):
            for num in freqToNum[i]:
                res.append(num)
                count+=1
                if count == k:
                    return res

        return res