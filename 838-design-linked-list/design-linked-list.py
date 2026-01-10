class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt 

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        node = self.head
        for i in range(index+1):
            node = node.next
            if node is None:
                return -1
        return node.val
            
    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        for i in range(index):
            node = node.next
            if not node:
                return
        new = ListNode(val, node.next)
        node.next = new
        
    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        for i in range(index):
            node = node.next
        if node and node.next:
            node.next = node.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)