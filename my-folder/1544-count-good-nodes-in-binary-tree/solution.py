# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Helper function to perform DFS and count good nodes
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Count this node as a good node if its value is greater than or equal to max_val
            good = 1 if node.val >= max_val else 0
            
            # Update the maximum value along the path
            max_val = max(max_val, node.val)
            
            # Recursively traverse the left and right subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good

        # Start DFS from the root, with the root's value as the initial maximum
        return dfs(root, root.val)

