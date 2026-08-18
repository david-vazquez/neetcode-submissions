class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the string dimmensions
        m = len(text1)
        n = len(text2)
        memory = [[-1]*n for _ in range(m)]
        
        # Recursive way no memoization
        def DFS(i, j):
            # Check if the position is valid
            if i>=m or j>=n:
                return 0
            
            # Check if the position is in memory
            if memory[i][j]>=0:
                return memory[i][j]

            # If the character is equal
            if text1[i]==text2[j]:
                # return 1 + the result of moving bought
                memory[i][j] = 1 + DFS(i+1, j+1)
                return memory[i][j]
            else:
                # Return the max of moving one on each
                memory[i][j] = max(DFS(i, j+1), DFS(i+1, j))
                return memory[i][j]

        return DFS(0,0)