# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # Helper function to perform DFS and track path sums
        def dfs(node, current_sum, prefix_sums):
            if not node:
                return 0
            
            # Update the current path sum by adding the current node's value
            current_sum += node.val
            
            # Find the number of valid paths that end at the current node
            # The number of such paths is equal to the number of times (current_sum - targetSum) has occurred
            path_count = prefix_sums.get(current_sum - targetSum, 0)
            
            # Update the prefix_sums dictionary with the current path sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recursively check the left and right subtrees
            path_count += dfs(node.left, current_sum, prefix_sums)
            path_count += dfs(node.right, current_sum, prefix_sums)
            
            # After returning from recursion, remove the current path sum from the prefix_sums
            # This step is critical to backtrack and not affect other paths
            prefix_sums[current_sum] -= 1
            
            return path_count
        
        # Dictionary to store prefix sums, initialized with 0 sum to handle the root path
        prefix_sums = {0: 1}
        
        # Start DFS from the root with an initial current_sum of 0
        return dfs(root, 0, prefix_sums)

