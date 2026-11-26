class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        best = float('-inf')

        for i in range(n-1, -1, -1):
            temp = arr[i]
            if best == float("-inf"):
                arr[i] = -1
            else:
                arr[i] = best
            best = max(best, temp)

        return arr