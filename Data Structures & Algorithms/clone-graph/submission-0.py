"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Corner cases
        if not node:
            return None

        # Clone map
        clones = {}
        
        def DFS(node):
            # If the node is cloned return it
            if node in clones:
                return clones[node]
        
            # We copy the node
            copy = Node(node.val)

            # Add the node to the clones map
            clones[node] = copy

            # Clone the neighbours
            for neighbour in node.neighbors:
                copy.neighbors.append(DFS(neighbour))
            
            # Return the copy
            return copy

        return DFS(node)

