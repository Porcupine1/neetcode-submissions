from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.data_store[key]
        
        l, r = 0, len(pairs) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if pairs[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        
        return pairs[r][1] if r >= 0 and pairs[r][0] <= timestamp else ""