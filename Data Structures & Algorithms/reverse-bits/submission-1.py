class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range (32):
            # Get the ith bit
            bit = (n>>i)&1
            # Set the 32-ith bit of the out
            out = out|(bit<<(31-i))
        return out