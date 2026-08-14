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
        clones[node] = Node(node.val)
        q = deque([node])
        
        # Copy nodes
        while q:
            # Get a node
            cur = q.popleft()

            # Process its neighbours
            for neighbour in cur.neighbors:
                # Clone the neighbour if needed
                if neighbour not in clones:
                    # Copy the node
                    clones[neighbour] = Node(neighbour.val)
                    # Add to the queue
                    q.append(neighbour)
                # Add the cloned neighbours to the cloned node
                clones[cur].neighbors.append(clones[neighbour])
            
        # Return the copy of node
        return clones[node]
