class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        maxPrefix = [0] * l
        maxSuffix = [0] * l

        p = height[0]
        s = height[-1]
        
        for i in range(1, l):
            maxPrefix[i] = max(p, height[i-1])
            maxSuffix[l-1 - i] = max(s, height[l-i])

            p = max(p, height[i-1])
            s = max(s, height[l-i])

        res = 0
        for j in range(l):
            water = min(maxPrefix[j], maxSuffix[j]) - height[j]

            if water > 0:
                res += water

        return res