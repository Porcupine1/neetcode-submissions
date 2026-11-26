from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for t in tasks:
            count[t] += 1
        dq = deque()
        cycles = 0
        hp = [-x for x in count.values()]
        heapq.heapify(hp)

        while hp or dq:
            cycles += 1
            if not hp:
                cycles = dq[0][1]
            else:
                val = heapq.heappop(hp)+1
                if val:
                    dq.append((val, cycles+n))

            if dq and cycles == dq[0][1]:
                heapq.heappush(hp, dq.popleft()[0])

        return cycles



        