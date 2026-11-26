class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def find_perms(curr, j, rem):
            if len(rem) == 0:
                res.append(curr[:])
                return

            for i in rem:
                curr[i] = nums[j]
                find_perms(curr, j+1, rem - {i})
                curr[i] = float("infinity")
        curr = [float("infinity")] * len(nums)
        rem = {i for i in range(len(nums))}
        find_perms(curr, 0, rem)
        return res