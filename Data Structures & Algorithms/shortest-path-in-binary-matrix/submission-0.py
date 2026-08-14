class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Get the grid size
        n = len(grid)

        # Start a que with the first position
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q = deque([(0, 0)])
        visited = set()
        length = 0
        visited.add((0,0))
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        while q:
            # Increase the length
            length += 1
            # Process all the positions in the que
            for i in range(len(q)):
                # Get the position
                r, c = q.popleft()
                # Check if we are at the end
                if c==r==n-1:
                    return length
                # Add its nighbours to the que
                for dr, dc in directions:
                    # Get the neighbour position
                    nr = r + dr
                    nc = c + dc
                    # Check the validity
                    if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
        
        # Return -1
        return -1





