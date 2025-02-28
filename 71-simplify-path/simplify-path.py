class Solution:
    def simplifyPath(self, path: str) -> str:
        path = list(filter(lambda x: x != "" and x != ".", path.split("/")))

        i = 0
        while i < len(path):
            if path[i] == "..":
                if i > 0:
                    path.pop(i-1) 
                    i -= 1 
                path.pop(i)
                i -= 1
            else:
                i += 1
            
            if i < 0:
                i = 0
        
        return "/" + "/".join(filter(lambda x: x, path))