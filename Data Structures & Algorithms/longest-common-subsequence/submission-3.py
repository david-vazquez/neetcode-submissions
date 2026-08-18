class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the string dimmensions
        m = len(text1)
        n = len(text2)
        prevRow = [0]*(n+1)
        

        for i in range(m-1, -1, -1):
            curRow = [0]*(n+1)
            for j in range(n-1, -1, -1):
                if text1[i]==text2[j]:
                # return 1 + the result of moving bought
                    curRow[j] = 1 + prevRow[j+1]
                else:
                    # Return the max of moving one on each
                    curRow[j] = max(curRow[j+1], prevRow[j])
            prevRow = curRow

        return prevRow[0]