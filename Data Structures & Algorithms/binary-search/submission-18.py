class Solution:
    def binarySearch(self, l, r, target, nums):
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(mid+1, r, target, nums)
        return self.binarySearch(l, mid-1, target, nums)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums)-1, target, nums)