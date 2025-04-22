class ListNode:
    def __init__(self, key=None, value=None, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.lru(key)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size == 0:
                self.head = ListNode(key=key, value=value)
                self.tail = self.head
                self.cache[key] = self.head
                self.size += 1
            else:
                self.head.prev = ListNode(key=key, value=value, nxt=self.head)
                self.head = self.head.prev
                self.cache[key] = self.head
                self.size += 1

                if self.size > self.capacity:
                    tail_prev = self.tail.prev
                    tail_prev.next = None
                    self.tail.prev = None
                    del self.cache[self.tail.key]
                    self.tail = tail_prev
                    self.size -= 1
        else:
            self.lru(key)
            self.cache[key].value = value


    def lru(self, key):
        node = self.cache[key]
        if node == self.head:
            return 

        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None

        node.next = self.head
        self.head.prev = node
        self.head = node

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)