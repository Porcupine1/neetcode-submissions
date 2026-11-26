import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0]*n
        used_rooms_until = []
        available_rooms = [i for i in range(n)]

        for start, end in meetings:
            while used_rooms_until and used_rooms_until[0][0] <= start:
                _, room = heapq.heappop(used_rooms_until)
                heapq.heappush(available_rooms, room)

            if not available_rooms:
                end_time, room = heapq.heappop(used_rooms_until)
                heapq.heappush(available_rooms, room)
                end = end_time + (end - start)

            room = heapq.heappop(available_rooms)
            heapq.heappush(used_rooms_until, (end, room))
            count[room] += 1
        
        return count.index(max(count))