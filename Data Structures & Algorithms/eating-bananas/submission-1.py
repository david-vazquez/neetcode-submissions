class Solution:
    def EatBananas(self, piles: List[int], k: int) -> int:
        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p/k)
        return totalTime
    
    def linearSearch(self, piles, h):
        for k in range(1, max(piles)+1):
            if self.EatBananas(piles, k)<=h:
                return k

    def binarySearch(self, piles, h, low, high):
        best = high

        while low<=high:
            M = low + (high-low)//2
            if self.EatBananas(piles, M) <= h:
                best = M
                high = M-1
            else:
                low = M+1
        return best
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return self.linearSearch(piles, h)
        return self.binarySearch(piles, h, 1, max(piles)+1)
