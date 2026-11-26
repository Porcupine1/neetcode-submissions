import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(hp, (-dist, [x, y]))
            if len(hp) > k:
                heapq.heappop(hp)

        return [point for _, point in hp]