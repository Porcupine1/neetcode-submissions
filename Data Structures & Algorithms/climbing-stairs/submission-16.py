class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 1

        for _ in range(1, n):
            temp = curr
            curr = curr+prev
            prev = temp

        return curr




