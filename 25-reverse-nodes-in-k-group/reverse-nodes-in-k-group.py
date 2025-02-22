# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2 or head == None:
            return head
        
        lenght = 0
        node = head
        while node:
            node = node.next
            lenght += 1
        
        nodes = []
        curr = head
        for i in range(int(lenght/k)):
            mid = []
            for _ in range(k):
                nxt = curr.next
                curr.next = None
                mid.append(curr)
                curr = nxt

            mid.reverse()
            nodes = nodes + mid
        
        nodes.append(curr)

        head = nodes.pop(0)
        curr = head
        for i in range(len(nodes)):
            curr.next = nodes[i]
            curr = curr.next

        return head 
                
            
