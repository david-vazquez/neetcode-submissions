class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        elements = []
        for p in points:
            elements.append([p[0]**2 + p[1]**2, p[0], p[1]])    

        heapq.heapify(elements)
        res = []
        for i in range(k):
            element = heapq.heappop(elements)
            res.append([element[1], element[2]])
        
        return res
