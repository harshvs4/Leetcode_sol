from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        # Queue to store nodes level by level
        queue = deque([root])
        right_view = []

        # Perform BFS level by level
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node of the current level, add it to the result
                if i == level_size - 1:
                    right_view.append(node.val)

                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view

