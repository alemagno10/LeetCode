class Node:
    def __init__(self, val=None, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
    
    def push(self, val):
        node = Node(val, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        return node
    
    def pop(self, node):
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next, node.prev = None, None

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.LL = LinkedList()
        self.uniques = {}

        for value in nums:
            self.add(value)

    def showFirstUnique(self) -> int:
        value = self.LL.head.next.val 
        return value if value is not None else -1 

    def add(self, value: int) -> None:
        if value not in self.uniques:
            self.uniques[value] = self.LL.push(value)
        else:
            self.LL.pop(self.uniques[value])
            self.uniques[value] = None


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

