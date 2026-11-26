class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        maxPrefix = [0] * l
        maxSuffix = [0] * l
        
        maxPrefix[0] = height[0]
        maxSuffix[-1] = height[-1]
        
        for i in range(1, l):
            maxPrefix[i] = max(maxPrefix[i-1], height[i])
            maxSuffix[l-1 - i] = max(maxSuffix[l-i], height[l-1-i])

        res = 0
        for j in range(l):
            water = min(maxPrefix[j], maxSuffix[j]) - height[j]

            if water > 0:
                res += water

        return res