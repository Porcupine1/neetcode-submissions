from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]
        
        dq = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                print("popped ", nums[dq[-1]])
                dq.pop()
                
            dq.append(r)
            print(dq)

            print("r: ", r)
            if r >= k-1:
                res.append(nums[dq[0]])
                print("res: ",res)
                l += 1
                if l > dq[0]:
                    dq.popleft()
        return res

