class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] <= nums[l + (r -l) // 2] <= nums[r]:
            return nums[0]

        while l < r:
            mid = l + (r - l) // 2
            print(nums[mid])
            if mid != 0 and nums[mid-1] > nums[mid]:
                print("here")
                return nums[mid]
            if mid < len(nums) -1 and nums[mid] > nums[mid+1]:
                print("here")
                return nums[mid+1]

            elif nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        print(l)
        return nums[l]