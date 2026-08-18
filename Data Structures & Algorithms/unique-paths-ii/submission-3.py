class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Edge cases
        if not obstacleGrid:
            return 0
        
        # Get the grid dimensions
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # Allocate memory for previous row
        prevRow = [0]*(cols+1)
        prevRow[-2] = 1

        # Compute row by row from the bottom
        for r in range(rows-1, -1, -1):
            curRow = [0]*(cols+1)
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c]:
                    curRow[c] = 0
                else:
                    curRow[c] = curRow[c+1] + prevRow[c]
            prevRow = curRow
        return prevRow[0]
