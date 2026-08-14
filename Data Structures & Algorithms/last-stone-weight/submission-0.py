class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            # Sort
            stones.sort()

            # Weight last 2
            last = stones.pop()
            lastlast = stones.pop()
            difference = last-lastlast

            # If equal remove them
            if difference:
                stones.append(difference)
        if len(stones)==1:
            return stones[0]
        else:
            return 0

