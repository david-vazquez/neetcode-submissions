class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the grid size
        n_rows = len(grid)
        n_cols = len(grid[0])

        # Find initial rotten fruits at t=0 and count the number of fresh fruits
        q = deque()
        n_fresh = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    n_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        # Set the timer to zero
        timer = -1
        if n_fresh == 0:
            return 0
        
        # Define the posible directions
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # While there are new rotten fruits
        while q:
            timer +=1

            # Process the que
            for i in range(len(q)):
                # Get one rotten fruit
                r, c = q.popleft()

                # Rotten neighbours
                for dr, dc in directions:
                    # Get the nighbour position
                    nr = r + dr
                    nc = c + dc

                    # Check if the neighbour is valid
                    if nr>=0 and nr<n_rows and nc>=0 and nc<n_cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        n_fresh -= 1
        
        # Return 
        if n_fresh == 0:
            return timer
        else:
            return -1






