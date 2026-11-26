"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hp = []
        intervals.sort(key=lambda x: x.start)

        for inter in intervals:
            if hp and hp[0] <= inter.start:
                heapq.heappop(hp)
                heapq.heappush(hp, inter.end)
            else:
                heapq.heappush(hp, inter.end)

        return len(hp)