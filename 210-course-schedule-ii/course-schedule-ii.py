from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for c,p in prerequisites:
            graph[c].add(p)
        
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            for req in graph[course]:
                if not dfs(req):
                    return False

            path.remove(course)
            visited.add(course)
            order.append(course)
            return True

        order = []
        visited, path = set(), set()
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order 

