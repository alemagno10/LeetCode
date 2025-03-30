class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0]*len(height)

        heighest = 0
        for i,wall in enumerate(height):
            if wall < heighest:
                water[i] = heighest - wall
            else:
                water[i] = 0
                heighest = wall
        
        heighest = 0
        for i in range(len(height)-1,-1,-1):
            wall = height[i]
            if wall < heighest:
                water[i] = min(water[i], heighest - wall)
            else:
                water[i] = 0
                heighest = wall
        
        return sum(water)

