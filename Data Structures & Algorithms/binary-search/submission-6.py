class Solution:

    def bisect(self, l, r, target, arr):
        mid = l + ((r-l)//2)
        if arr[mid] == target:
            return mid
        if l >= r:
            return -1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        mid = l + ((r-l)//2)
        return self.bisect(l, r, target, arr)

    def search(self, nums: List[int], target: int) -> int:
        return self.bisect(0, len(nums)-1, target, nums)