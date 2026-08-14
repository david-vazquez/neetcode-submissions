# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightAndBalance(root):
            if not root:
                return 0

            leftH = heightAndBalance(root.left)
            if leftH < 0:
                return -1
            rightH = heightAndBalance(root.right)
            if rightH < 0:
                return -1
            if abs(leftH-rightH)>1:
                return -1
            else:
                return max(leftH, rightH)+1
        
        return heightAndBalance(root)>=0