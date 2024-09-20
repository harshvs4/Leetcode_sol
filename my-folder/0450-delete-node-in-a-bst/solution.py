# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted is found
            # Case 1: Node has no children or only one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 2: Node has two children
            # Find the inorder successor (smallest value in the right subtree)
            min_node = self.findMin(root.right)
            root.val = min_node.val  # Replace value with inorder successor's value
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    # Helper function to find the minimum value node in a subtree
    def findMin(self, node):
        while node.left:
            node = node.left
        return node

