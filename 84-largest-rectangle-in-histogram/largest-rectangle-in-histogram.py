class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i,height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                prevH, prevI = stack.pop()
                area = max(area, prevH*(i-prevI))
                start = prevI
            stack.append((height,start))

        for height,i in stack: 
            area = max(area, height*(len(heights)-i))
            
        return area