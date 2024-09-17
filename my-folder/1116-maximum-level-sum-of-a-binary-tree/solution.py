# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])
        maxi = float('-inf')
        count = 1
        x = -1
        while queue:
            l = len(queue)
            s = 0
            for i in range(l):
                node = queue.popleft()
                s += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if s > maxi:
                maxi = s
                x = count
            count+=1

        return x


        
