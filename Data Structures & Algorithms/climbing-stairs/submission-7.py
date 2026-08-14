class Solution:
    def climbStairs(self, n: int) -> int:
        # Simple cases
        if n<=2:
            return n
        
        # Initialize the DP array
        lastlast = 1
        last = 2

        # Climb
        for i in range(3, n+1):
            tmp = last
            last = last + lastlast
            lastlast = tmp
        return last

