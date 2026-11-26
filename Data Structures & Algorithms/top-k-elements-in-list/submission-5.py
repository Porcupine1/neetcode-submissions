from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        top_k_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k]

        return [item[0] for item in top_k_items]