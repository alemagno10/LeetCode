# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        curr = head
        while curr:
            nxt = curr.next
            curr.next = None
            nodes.append(curr)
            curr = nxt
        
        i,j = 0,1
        while j < len(nodes):
            nodes[i], nodes[j] = nodes[j], nodes[i]
            i += 2
            j += 2
        
        head = nodes.pop(0)
        curr = head
        for node in nodes:
            curr.next = node
            curr = node
        
        return head


