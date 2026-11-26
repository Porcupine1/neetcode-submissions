class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, e in enumerate(temperatures):
            while stack and e > stack[-1][1]:
                index, _ = stack.pop()
                result[index] = i - index
            stack.append((i, e))

        return result