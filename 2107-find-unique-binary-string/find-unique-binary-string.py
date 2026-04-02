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

        stack = [(trie.root, [])]
        while True:
            node, curr = stack.pop()
            if node.isEnd:
                continue
            if len(node.children) < 2:
                valid = curr + ["0" if "1" in node.children else "1"]
                valid.extend(["0"]*(len(nums)-len(valid)))
                return "".join(valid)

            stack.append((node.children["1"], curr + ["1"]))
            stack.append((node.children["0"], curr + ["0"]))
            