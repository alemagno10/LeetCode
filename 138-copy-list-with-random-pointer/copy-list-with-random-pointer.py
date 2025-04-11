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
        dummy = Node(0)
        newNode = dummy

        nodesPos = {}
        randomPos = {}
        newNodes = []

        node, i = head, 0
        while node:
            new = Node(node.val)
            newNode.next = new
            newNodes.append(new)

            nodesPos[node] = i
            node = node.next
            newNode = newNode.next
            i+=1

        node = head
        while node:
            randomPos[node] = nodesPos[node.random] if node.random else -1
            node = node.next
        
        newNode = dummy.next
        node = head
        while newNode:
            newNode.random = newNodes[randomPos[node]] if randomPos[node] >= 0 else None
            node = node.next
            newNode = newNode.next

        return dummy.next