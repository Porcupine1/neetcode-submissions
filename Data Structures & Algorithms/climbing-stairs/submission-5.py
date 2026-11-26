class Solution:
    def count(self, n, ones, twos):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        ones = self.count(n-1, ones, twos)
        twos = self.count(n-2, ones, twos)
        return ones + twos

    def climbStairs(self, n: int) -> int:
        ones = 1
        twos = 0 if n == 1 else 2
        return self.count(n, ones, twos)

        