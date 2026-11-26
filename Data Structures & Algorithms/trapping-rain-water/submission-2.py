class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax, rightMax, res = height[l], height[r], 0
        
        while l < r:
            if height[l] < height[r]:
                l += 1
                water = leftMax - height[l]
                leftMax = max(leftMax, height[l])
            else:
                r -= 1 
                water = rightMax - height[r]
                rightMax = max(rightMax, height[r])
            if water > 0:
                res += water

        return res