from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = deque()
        res = [0] * len(temperatures)


        for idx, temp in enumerate(temperatures):
            while queue and temp > queue[0][1]:
                idx2, _ = queue.popleft()
                res[idx2] = idx - idx2
            else:
                queue.appendleft((idx, temp))

        return res
        