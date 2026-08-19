class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range (32):
            # Get the last bit
            last_bit = n&1
            # Shift it right
            n = n>>1
            # Shift left the out
            out = out<<1
            # Set the last bit of the out
            out = out|last_bit
        return out
