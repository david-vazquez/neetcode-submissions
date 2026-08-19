class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBits(n):
            count = 0
            while n>0:
                if n&1:
                    count += 1
                n = n >> 1
            return count

        out = []
        for i in range(n+1):
            out.append(countBits(i))
        
        return out
