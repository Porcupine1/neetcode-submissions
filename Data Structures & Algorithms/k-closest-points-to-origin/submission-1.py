import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close = []
        for x,y in points:
            heapq.heappush(close, (-math.sqrt(x**2+y**2),[x,y]))
            if len(close) > k:
                heapq.heappop(close)
 
        return [point for _, point in close]