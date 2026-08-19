class Solution:
    def countBits(self, n: int) -> List[int]:
        # We start the solution to all zeros
        out = [0]*(n+1)

        # We compute the number of bits for each number based on previous ones
        offset = 1
        for i in range(1,n+1):
            # Check if the number is a power of 2
            if offset*2 == i:
                offset = i
            # Compute
            out[i] = 1 + out[i-offset]
        return out
