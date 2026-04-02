class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode("-1")
    
    def add(self, val):
        node = self.root
        for char in val:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode(char)
                node = node.children[char]
        node.isEnd = True

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        trie = Trie()
        for binary in nums:
            trie.add(binary)
        
        def dfs(root, curr):
            nonlocal valid 
            if root.isEnd:
                return
            if len(root.children) < 2:
                valid = curr + [root.val, "0" if "1" in root.children else "1"]
                return
            curr.append(root.val)
            dfs(root.children["0"],curr)
            dfs(root.children["1"],curr)
            curr.pop()
        
        valid = []
        dfs(trie.root, [])
        return "".join(valid[1:]+["0"]*(len(nums)-len(valid)+1))


