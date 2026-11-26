import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*num for num in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x,y = -1*heapq.heappop(stones), -1*heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, -abs(x-y))
        
        return -stones[0] if stones else 0