class TrieNode:
    def __init__(self, id=None):
        self.children = {}
        self.end = False
        self.id = id

class Trie:
    def __init__(self):
        self.head = TrieNode()
    
    def add(self, i, word):
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
        node.id = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        res, visited = list(), set()
        trie = Trie()
        
        def inbound(x,y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        def dfs(node,x,y):
            if node.end:
                res.append(words[node.id])
                node.end = False

            key, c = (x,y), board[x][y] if inbound(x,y) else None
            if (c is None) or (c not in node.children) or (key in visited):
                return False

            visited.add(key)
            for dx,dy in moves:
                dfs(node.children[c], x+dx, y+dy)
            visited.remove(key)
        
        for i,word in enumerate(words):
            trie.add(i,word)

        for i in range(len(board)):
            for j in range(len(board[0])): 
                dfs(trie.head,i,j)

        return res

