# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalanced = True

        def heightAndBalance(root):
            if not root:
                return 0, True

            leftH, leftB = heightAndBalance(root.left)
            rightH, rightB = heightAndBalance(root.right)
            rootH = max(leftH, rightH)+1
            rootB = leftB and rightB and abs(leftH-rightH)<=1
            return rootH, rootB
        
        h, b = heightAndBalance(root)
        return b



            