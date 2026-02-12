class ListNode:
    def __init__(self, key=None, prev=None, nxt=None):
        self.key = key
        self.prev = prev
        self.next = nxt

class LinkedList:
    def __init__(self, capacity, cache):
        self.head = ListNode()
        self.tail = ListNode(prev=self.head)
        self.head.next = self.tail
        self.capacity = capacity
        self.cache = cache
    
    def push(self, key):
        if key in self.cache:
            self.pop(key)
        elif len(self.cache) == self.capacity:
            self.pop()

        node = ListNode(key,self.tail.prev,self.tail)
        node.prev.next = node
        self.tail.prev = node
        self.cache[key] = node
            
    def pop(self, key=None):
        if len(self.cache) == 0:
            return
        node = self.cache[key] if key is not None else self.head.next
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]
    
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.map = {}
        self.list = LinkedList(capacity, self.cache)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.list.push(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        self.list.push(key)
        self.map[key] = value        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)