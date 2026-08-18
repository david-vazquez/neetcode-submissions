class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Edge cases
        if not obstacleGrid:
            return 0
        
        # Get the grid dimensions
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # Allocate memory for memoization
        memory = [[-1]*cols for _ in range(rows)]

        # DFS approach with recursion
        def DFS(r, c):
            # Check if the positon is invalid
            if r>=rows or c>=cols or obstacleGrid[r][c]==1:
                return 0
            
            # Check if we have arrived to the goal
            if r==rows-1 and c==cols-1:
                return 1

            # Check if the solution is in memory
            if memory[r][c]>=0:
                return memory[r][c]
            
            # Compute for the middle
            value = DFS(r+1, c) + DFS(r, c+1)
            memory[r][c] = value
            return value
        
        # Call from the starting point
        return DFS(0,0)
