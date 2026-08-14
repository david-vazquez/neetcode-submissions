# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.out = 0

        def DFS(root, k):
            # empty nodes
            if not root:
                return
            
            # traverse left
            DFS(root.left, k)
            # process current node
            self.cnt += 1
            if self.cnt == k:
                self.out = root.val
            # traverse right
            DFS(root.right, k)
        
        DFS(root, k)
        return self.out

            

      