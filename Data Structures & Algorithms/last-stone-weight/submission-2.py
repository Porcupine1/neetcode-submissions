import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-x for x in stones]
        heapq.heapify(hp)

        while len(hp) > 1:
            x = heapq.heappop(hp)
            y = heapq.heappop(hp)
            if x - y != 0:
                heapq.heappush(hp, -abs(x-y))

        return -hp[0] if len(hp) > 0 else 0