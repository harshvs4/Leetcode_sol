# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_zigzag = 0  # To track the longest zigzag path
    
    def maxZig(self, node, direction, count):
        if node is None:
            return
        
        # Update the maximum zigzag length encountered so far
        self.max_zigzag = max(self.max_zigzag, count)
        
        # Continue the zigzag
        if direction == 'left':
            # If we're going left, next we try to go right
            self.maxZig(node.left, 'left', 1)  # Reset the count when starting a new zigzag
            self.maxZig(node.right, 'right', count + 1)  # Continue the zigzag to the right
        else:
            # If we're going right, next we try to go left
            self.maxZig(node.right, 'right', 1)  # Reset the count when starting a new zigzag
            self.maxZig(node.left, 'left', count + 1)  # Continue the zigzag to the left

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Start the zigzag from both left and right directions
        self.maxZig(root, 'left', 0)
        self.maxZig(root, 'right', 0)
        
        return self.max_zigzag

