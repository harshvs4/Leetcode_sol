# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, arr):
        if not node:
            return
        
        # Traverse left subtree
        self.dfs(node.left, arr)
        
        # Check if the current node is a leaf
        if not node.left and not node.right:
            arr.append(node.val)  # Visit leaf node (print or store it)
        
        # Traverse right subtree
        self.dfs(node.right,arr)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        self.dfs(root1, arr1)
        self.dfs(root2, arr2)

        return arr1 == arr2


