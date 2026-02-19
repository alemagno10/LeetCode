from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        positions = defaultdict(int)

        for row in wall:
            pos = 0
            for length in row[:-1]:
                pos += length
                positions[pos] += 1    

        return len(wall) - (max(positions.values()) if positions else 0)