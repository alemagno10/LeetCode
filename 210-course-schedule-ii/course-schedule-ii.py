from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for c,p in prerequisites:
            graph[c].add(p)
        
        def dfs(course, visited):
            if course in visited:
                return False
            if course in order:
                return True

            visited.add(course)
            for req in graph[course]:
                if not dfs(req, visited):
                    return False

            visited.remove(course)
            completed.add(course)
            order.append(course)
            return True

        order, completed = [], set()
        for course in range(numCourses):
            if not dfs(course, set()):
                return []
        
        return order 

