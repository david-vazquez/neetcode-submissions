class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the grid size
        n_rows = len(grid)
        n_cols = len(grid[0])

        # Set the max area to zero
        max_area = 0

        def DFS(r,c):
            # Check if we are in the water
            if r<0 or r>=n_rows or c<0 or c>=n_cols or grid[r][c] == 0:
                return 0
 
            # Mark it as water, and set area to one
            grid[r][c] = 0
            area = 1

            # Add the area of the neighbours
            area += DFS(r+1,c)
            area += DFS(r-1,c)
            area += DFS(r,c+1)
            area += DFS(r,c-1)

            # Return the area
            return area

        # Search for islands 
        for r in range(n_rows):
            for c in range(n_cols):
                # If an island is found, measure its area
                if grid[r][c] == 1:
                    max_area = max(max_area, DFS(r,c))
        
        # Return the max area
        return max_area