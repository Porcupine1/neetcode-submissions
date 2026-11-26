class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        curr = sum(arr[:k])
        res = 1 if curr/k >= threshold else 0
        for r in range(k, len(arr)):
            curr -= arr[l]
            curr += arr[r]
            l += 1
            res += int(curr/k >= threshold)

        return res
