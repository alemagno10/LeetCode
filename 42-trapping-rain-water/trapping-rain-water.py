class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l, r = 0, len(heights)-1
        maxL, maxR = heights[l], heights[r]
        res = 0

        while l < r:
            if heights[l] < heights[r]:
                l += 1
                amount = maxL - heights[l]
                if amount > 0:
                    res += amount
                maxL = max(maxL, heights[l])
            else:
                r -= 1
                amount = maxR - heights[r]
                if amount > 0:
                    res += amount
                maxR = max(maxR, heights[r])

        return res

            
        
                
                

