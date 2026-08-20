class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Corner cases
        n = len(arr)
        if n<k:
            return 0
        
        # We sum the first k values
        windowSum = 0
        threshold *= k
        count = 0

        # We move the window till the end of the array
        for R in range(n):
            # Add the element
            windowSum += arr[R]

            # If it is too big remove an element
            if R>=k-1:
                # Check the window average
                if windowSum>=threshold:
                    count += 1
                windowSum -= arr[R - k + 1]
        
        # Return the count
        return count
            

            
            


