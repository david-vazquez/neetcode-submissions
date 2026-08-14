# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def root_to_leaf_sum(root, target, total):
            # NULL case
            if not root:
                return False
            
            # Add this node value
            total += root.val
        
            # Leaf case
            if not root.left and not root.right and total == target:
                return True
            
            # Left node case
            if root_to_leaf_sum(root.left, target, total):
                return True

            # Right node case
            if root_to_leaf_sum(root.right, target, total):
                return True

            # Backtrack
            #total -= root.val
            return False
        
        return root_to_leaf_sum(root, targetSum, 0)

