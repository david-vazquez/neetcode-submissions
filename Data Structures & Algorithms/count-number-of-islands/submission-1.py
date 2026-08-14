class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the grid size
        n_rows = len(grid)
        n_cols = len(grid[0])
        n_islands = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Breath first search
        def BFS(r, c):
            # Start with the first point
            q = deque([(r, c)])
            grid[r][c] = '0'

            while q:
                # Get a point from the que
                r, c = q.popleft()

                # Add its neighbours to the que
                for dr, dc in directions:
                    # Get neighbour position
                    nr = r + dr
                    nc = c + dc
                    # Check if it is a valid land
                    if nr>=0 and nr<n_rows and nc>=0 and nc<n_cols and grid[nr][nc] == '1':
                        q.append((nr, nc))
                        grid[nr][nc] = '0'


        # Look for the islands
        for r in range(n_rows):
            for c in range(n_cols):
                # If an island is found
                if grid[r][c] == '1':
                    # Increment the number of islands
                    n_islands += 1
                    # Remove all the land from that island
                    BFS(r,c)
        
        # Return the number of islands
        return n_islands
        