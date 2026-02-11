class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: math.sqrt(p[0]**2+p[1]**2))[:k]