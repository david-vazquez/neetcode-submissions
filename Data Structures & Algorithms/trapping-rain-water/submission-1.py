class Solution:
    def trap(self, height: List[int]) -> int:
        # Init the areas
        L=0
        R=len(height)-1
        totalArea = 0
        leftMax = 0
        rightMax = 0

        # Move pointers
        while L<R:
            leftMax = max(leftMax, height[L])
            rightMax = max(rightMax, height[R])
            if leftMax<=rightMax:
                totalArea += leftMax-height[L]
                L+=1
            else:
                totalArea += rightMax-height[R]
                R-=1
        
        # Return the area
        return totalArea
