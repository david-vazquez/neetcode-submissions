class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memory allocation if you do memopization
        memory = [[0]*n for i in range(m)]

        # Recursive approach. No momization.
        def DFS(r, c, memory):
            # Out of the board
            if r>=m or c>=n:
                return 0
            # Reached the goal
            if r==m-1 and c==n-1:
                return 1
            # Get it from the cache if exists
            if memory[r][c] > 0:
                return memory[r][c]
            
            # In the middle: Move right or bottom
            memory[r][c] = DFS(r+1, c, memory) + DFS(r,c+1, memory)
            return memory[r][c]
        
        # Call the recursive function
        return DFS(0, 0, memory)