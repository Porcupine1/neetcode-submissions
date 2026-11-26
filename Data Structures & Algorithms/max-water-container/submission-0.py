class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxArea = 0
        currArea = 0

        while l < r:
            currArea = (r - l) * min(height[r], height[l])
            maxArea = max(maxArea, currArea)

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
            
        return maxArea