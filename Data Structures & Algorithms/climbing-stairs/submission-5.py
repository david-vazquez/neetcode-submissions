class Solution:
    def climbStairs(self, n: int) -> int:
        # Simple cases
        if n<=2:
            return n
        
        # Initialize the DP array
        DP = [0]*(n+1)
        DP[1] = 1
        DP[2] = 2

        # Climb
        for i in range(3, n+1):
            DP[i] = DP[i-1] + DP[i-2]
        return DP[n]

