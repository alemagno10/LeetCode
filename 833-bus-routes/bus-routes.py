from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = self.createGraph(routes)
        visitedLines, visitedStops = set(), set()

        queue = deque([(source,0)])
        while queue:
            curr, buses = queue.popleft()
            if curr == target:
                return buses

            if curr in visitedStops:
                continue

            visitedStops.add(curr)
            for line in graph[curr]:
                if line in visitedLines:
                    continue
                for stop in routes[line]:
                    queue.append((stop,buses+1))
                visitedLines.add(line)

        return -1

    def createGraph(self, routes: List[List[int]]):
        graph = defaultdict(set)
        for i,route in enumerate(routes):
            for j, stop in enumerate(route):
                graph[stop].add(i)
        return graph