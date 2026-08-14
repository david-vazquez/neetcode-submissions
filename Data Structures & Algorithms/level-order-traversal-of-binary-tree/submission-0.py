# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        queue = deque()
        queue.append(root)
        level = 0

        while len(queue) > 0:
            out_this_layer = []
            for i in range(0,len(queue)):
                node = queue.popleft()
                out_this_layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            out.append(out_this_layer)
        
        return out

            

