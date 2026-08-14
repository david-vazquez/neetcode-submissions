class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}
        def DFS(i):
            # Base case: We finish the stairs
            if i==n:
                return 1
            elif i>n:
                return 0
            else:
                # Add memoization
                if i in cache:
                    return cache[i]
                else:
                    cache[i] = DFS(i+1) + DFS(i+2)
                    return cache[i]
        
        return DFS(0)
