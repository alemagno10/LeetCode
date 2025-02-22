# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for head in lists:
            node = head
            while node:
                nxt = node.next
                node.next = None
                nodes.append(node)
                node = nxt

        if len(nodes) == 0:
            return None

        nodes.sort(key=lambda x: x.val)

        head = nodes.pop(0)
        node = head
        for next_node in nodes:
            node.next = next_node
            node = next_node

        return head
        