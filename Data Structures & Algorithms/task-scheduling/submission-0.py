import heapq
from collections import defaultdict, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        mp = defaultdict(int)
        time = 0

        for v in tasks:
            mp[v] -= 1
        hp = [v for v in mp.values()]
        heapq.heapify(hp)

        while q or hp:
            time += 1

            if not hp:
                time = q[0][1]
            else: 
                count = 1+ heapq.heappop(hp)
                if count:
                    q.append([count, time+n])
            if q and q[0][1] == time:
                heapq.heappush(hp, q.popleft()[0])

        return time

