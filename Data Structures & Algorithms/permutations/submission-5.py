class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        res = []

        def findPerms(curr, currLen, visited):
            if currLen == numsLen:
                res.append(curr[:])
                return 

            for j in range(len(nums)):
                if not visited[j]:
                    visited[j] = True
                    findPerms(curr+[nums[j]], currLen+1, visited)
                    visited[j] = False

        visited = [False for _ in range(len(nums))]
        findPerms([], 0, visited)
        return res