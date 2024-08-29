"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        queue = deque([root])

        while queue:
            previous_node = None
            queue_len = len(queue)

            for _ in range(queue_len):
                node = queue.popleft()
                
                # Connect the previous node's next to the current node
                if previous_node:
                    previous_node.next = node
                
                # Update previous_node to the current node
                previous_node = node

                # Enqueue left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Ensure the last node in this level points to None
            previous_node.next = None

        return root

