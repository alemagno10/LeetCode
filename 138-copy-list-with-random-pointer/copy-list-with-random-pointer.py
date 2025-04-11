"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper = {None:None}

        node = head
        while node:
            new = Node(node.val)
            mapper[node] = new
            node = node.next

        node = head
        while node:
            new = mapper[node]
            new.next = mapper[node.next]
            new.random = mapper[node.random]
            node = node.next
        
        return mapper[head]

