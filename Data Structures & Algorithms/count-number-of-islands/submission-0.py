class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the grid size
        n_rows = len(grid)
        n_cols = len(grid[0])
        n_islands = 0

        def DFS(r, c):
            # Base condition: In water or out of grid
            if r<0 or r>=n_rows or c<0 or c>=n_cols or grid[r][c] == '0':
                return
            
            # Remove this land
            grid[r][c] = '0'

            # Visit neighbours
            DFS(r+1, c)
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r, c-1)
            return

        # Look for the islands
        for r in range(n_rows):
            for c in range(n_cols):
                # If an island is found
                if grid[r][c] == '1':
                    # Increment the number of islands
                    n_islands += 1
                    # Remove all the land from that island
                    DFS(r,c)
        
        # Return the number of islands
        return n_islands