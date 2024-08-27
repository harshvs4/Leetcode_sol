# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, root.val)])  # Queue stores pairs of (node, current path sum)

        while queue:
            node, current_sum = queue.popleft()

            # Check if we're at a leaf node and the current path sum equals targetSum
            if not node.left and not node.right and current_sum == targetSum:
                return True

            # If left child exists, add it to the queue with updated path sum
            if node.left:
                queue.append((node.left, current_sum + node.left.val))

            # If right child exists, add it to the queue with updated path sum
            if node.right:
                queue.append((node.right, current_sum + node.right.val))

        return False
        
