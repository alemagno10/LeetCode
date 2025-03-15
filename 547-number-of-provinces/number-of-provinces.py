from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] and i!=j:
                    provinces[i].append(j)
        
        visited = set()
        def dfs(city):
            if city in visited:
                return 
            visited.add(city)
            for neighbor in provinces[city]:
                dfs(neighbor)

        numOfProvinces = 0
        for city in range(len(isConnected)):
            if city not in visited:
                numOfProvinces += 1
                dfs(city) 
        
        return numOfProvinces

