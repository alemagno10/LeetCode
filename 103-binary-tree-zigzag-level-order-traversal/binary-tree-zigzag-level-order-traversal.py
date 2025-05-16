# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([(root,0)])
        depth = 0
        res = [[]]

        while len(queue) > 0:
            if depth % 2 != 0:
                if queue[0] and queue[0][1] > depth:
                    depth += 1
                    res.append([])
            else:
                if queue[-1] and queue[-1][1] > depth:
                    depth += 1
                    res.append([])
            
            curr = queue.popleft() if depth % 2 != 0 else queue.pop()
            res[-1].append(curr[0].val)
            
            if depth % 2 != 0:
                if curr[0].right: queue.append((curr[0].right, depth+1))
                if curr[0].left: queue.append((curr[0].left, depth+1))
            else:
                if curr[0].left: queue.appendleft((curr[0].left, depth+1))
                if curr[0].right: queue.appendleft((curr[0].right, depth+1))

        return res