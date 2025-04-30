class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for c,d in prerequisites: 
            graph[c].append(d)

        # states: unvisited; visiting; visited
        visited, path = set(), set()

        output = []
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for adj in graph[course]:
                if not dfs(adj):
                    return False

            path.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output