class Solution:

    def bisect(self, l, r, target, arr):
        if l > r:
            return -1
        
        mid = l + ((r-l)//2)
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return self.bisect(mid + 1, r, target, arr)
        return self.bisect(l, mid - 1, target, arr)

    def search(self, nums: List[int], target: int) -> int:
        return self.bisect(0, len(nums)-1, target, nums)