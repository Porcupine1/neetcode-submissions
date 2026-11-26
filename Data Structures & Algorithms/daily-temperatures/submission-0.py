class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, e in enumerate(temperatures):
            while stack and e > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)

        return result        