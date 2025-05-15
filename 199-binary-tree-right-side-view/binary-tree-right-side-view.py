# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:       
        if not root:
            return []
    
        queue = deque([(root,0)])
        mostRight = (root,0)
        res = []
        depth = 0

        while len(queue) > 0:
            curr = queue.popleft()
            if curr[1] > depth:
                res.append(mostRight[0].val)
                depth += 1
            
            mostRight = curr

            if curr[0].left:
                queue.append((curr[0].left, depth+1))
                        
            if curr[0].right:
                queue.append((curr[0].right, depth+1))
        
        res.append(mostRight[0].val)
        return res


        