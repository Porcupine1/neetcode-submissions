class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        # find the index of the min first value 
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        index = l
        print(index)
        bounds = [((0, index-1))] if index > 0 else []
        bounds.append((index, len(nums)-1))
        for bound in bounds:
            l, r = bound
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
        return -1