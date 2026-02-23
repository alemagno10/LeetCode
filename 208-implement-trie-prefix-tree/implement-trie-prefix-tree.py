class TreeNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TreeNode()
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c] 

    def search(self, word: str) -> bool:
        node = self.head
        if word not in self.words:
            return False

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c] 
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c] 
        return True
        