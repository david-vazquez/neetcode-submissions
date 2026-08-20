class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # We start with the biggest posible value
        minLength = float('inf')
        L=0
        windowSum = 0

        # Move the window
        for R in range(len(nums)):
            # We add the number to the sum
            windowSum += nums[R]

            # Check the window sum
            while windowSum>=target:
                # Update the min length
                minLength = min(minLength, R-L+1)
                # Srink the window by the left
                windowSum -= nums[L]
                L += 1
        
        # Return the values
        if minLength == float('inf'):
            return 0
        else:
            return minLength


