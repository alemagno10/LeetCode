class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]

        def find(node):
            """
            Return the group that a node belongs.
            """
            if node != parents[node]:
                return find(parents[node])
            return parents[node]

        def union(n1, n2):
            """
            Unions groups containing n1 and n2.
            Return whether nodes are connected (have a same parent).
            """ 
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            a,b = min(p1,p2), max(p1,p2)
            parents[a] = b
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        