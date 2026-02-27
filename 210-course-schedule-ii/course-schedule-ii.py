from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0]*numCourses
        noprerequisites = set(range(numCourses))
        res = []

        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
            degree[a] += 1
            if a in noprerequisites:
                noprerequisites.remove(a)
        
        queue = deque(noprerequisites)
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for d in graph[curr]:
                degree[d] -= 1
                if degree[d] == 0:
                    queue.append(d)

        return res if sum(degree) == 0 else []