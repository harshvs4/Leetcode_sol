# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        root1.val += root2.val

        queue = deque([(root1, root2)])

        while queue:
            p1, p2 = queue.popleft()

            # Process left children
            if p1.left and p2.left:
                p1.left.val += p2.left.val
                queue.append((p1.left, p2.left))
            elif p1.left is None:
                p1.left = p2.left

            # Process right children
            if p1.right and p2.right:
                p1.right.val += p2.right.val
                queue.append((p1.right, p2.right))
            elif p1.right is None:
                p1.right = p2.right

        return root1

