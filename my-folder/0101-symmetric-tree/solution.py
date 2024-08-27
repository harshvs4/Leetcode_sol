# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [[root.left, root.right]]
        while queue:
            pair = queue.pop(0)
            left, right = pair[0], pair[1]
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                queue.append([left.left, right.right])
                queue.append([left.right, right.left])
            else:
                return False
        return True
        
