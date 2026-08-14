class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones)>1:
            # Sort
            #stones.sort()

            # Weight last 2
            last = heapq.heappop_max(stones)
            lastlast = heapq.heappop_max(stones)
            difference = last-lastlast

            # If equal remove them
            if difference:
                heapq.heappush_max(stones, difference)
        if len(stones)==1:
            return stones[0]
        else:
            return 0

