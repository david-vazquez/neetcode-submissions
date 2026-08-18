class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memory allocation for previous row
        prevRow = [0]*n

        # Compute from the bottom row up
        for r in range(m-1, -1, -1):
            # Allocate memory for this row
            curRow = [0]*n
            curRow[-1] = 1
            # Compute from right to left
            for c in range(n-2, -1, -1):
                curRow[c] = curRow[c+1] + prevRow[c]
            # Switch rows
            prevRow = curRow
        
        # Return the first position
        return prevRow[0]