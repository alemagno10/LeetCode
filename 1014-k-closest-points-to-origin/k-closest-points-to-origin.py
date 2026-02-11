class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x,y: math.sqrt(x**2 + y**2)
        distances = [(euclidean(x,y),[x,y]) for x,y in points]
        distances.sort(key=lambda x: x[0])
        return [d[1] for d in distances[:k]]