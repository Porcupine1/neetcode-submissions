class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        widthsToRight = [1] * len(heights)
        widthsToLeft = [1] * len(heights)

        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                j = stack.pop()
                widthsToRight[j] = i - j
            while stack and i == len(heights)-1 and h >= heights[stack[-1]]:
                j = stack.pop()
                widthsToRight[j] += i - j
            stack.append(i)

        heights.reverse()
       
        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                j = stack.pop()
                widthsToLeft[j] = i - j
            while stack and i == len(heights) -1 and h >= heights[stack[-1]]:
                j = stack.pop()
                print('here')
                widthsToLeft[j] += i - j
            stack.append(i)
        
        widthsToLeft.reverse()
        print( widthsToRight)
        print( widthsToLeft)
        
        return max([h * (widthsToLeft[i] + widthsToRight[i] - 1) for i, h in enumerate(heights[::-1])])