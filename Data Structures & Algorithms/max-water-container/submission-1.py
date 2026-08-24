class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start variables
        maxArea = 0
        L = 0
        R = len(heights)-1

        # Move the pointers
        while L<R:
            # Compute the current area
            height = min(heights[L], heights[R])
            width = R-L
            area = width*height
            maxArea = max(area, maxArea)

            # Move one pointer
            if heights[L]<=heights[R]:
                L += 1
            else:
                R -= 1
        
        # Return the area
        return maxArea

