# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0

        if root is None:
            return 0

        queue = [root]

        while queue:
            node = queue.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    s += node.left.val
                else:
                    queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return s
        
