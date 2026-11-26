import heapq
class MedianFinder:

    def __init__(self):
        self.r = []
        self.l = []
        

    def addNum(self, num: int) -> None:
        if not self.l or num <= -self.l[0]:
            heapq.heappush(self.l, -num)
        else:
            heapq.heappush(self.r, num)

        if len(self.l) > len(self.r)+1:
            heapq.heappush(self.r, -heapq.heappop(self.l))
        elif len(self.r) > len(self.l):
            heapq.heappush(self.l, -heapq.heappop(self.r))
        print(self.l, self.r)
        

    def findMedian(self) -> float:
        if len(self.l) == len(self.r):
            return (self.r[0] - self.l[0])/2
        return -self.l[0]
        
        