class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True, key=lambda pair: pair[0])
        time_0 = (target - pairs[0][0])/pairs[0][1]
        fleets = 1
        for p, s in pairs[1:]:
            time_1 = (target - p)/s
            if time_1 > time_0:
                fleets += 1
                time_0 = time_1
        
        return fleets