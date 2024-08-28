# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])  # Start with the root node in the queue

        while queue:
            current_node = queue.popleft()

            # Swap the left and right children
            current_node.left, current_node.right = current_node.right, current_node.left

            # Add the children to the queue for further processing
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return root
        
