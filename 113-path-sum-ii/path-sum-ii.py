# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, target):
            if not root:
                return []    

            target -= root.val
            if target == 0 and not root.left and not root.right:
                return [[root.val]]

            output = []
            left, right = dfs(root.left, target), dfs(root.right, target)

            if left:
                for sub in left:
                    sub.insert(0, root.val)
                output += left
            
            if right:
                for sub in right:
                    sub.insert(0, root.val)
                output += right
            
            print(output)
            return output  

        return dfs(root, targetSum)       
            
            