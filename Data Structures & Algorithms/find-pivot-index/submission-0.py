class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        prefix = [0]*size
        suffix = [0]*size

        for i in range(1, size):
            prefix[i] = prefix[i-1] + nums[i-1]
        for i in range(size-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i+1]

        print(prefix, suffix)
        for i in range(size):
            if prefix[i] == suffix[i]:

                return i

        return -1