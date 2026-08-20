class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # abs(i-j)<=k --> Two numbers in a window of size 2K
        # nums[i]=nums[j] --> At least 2 equal numbers
        # Question: Are there any windows of size k with 2 equal numbers?

        # Check corner cases
        if k==0:
            return False
        
        # We use a set to store the values in the window O(1) to access or delete
        window = set()

        # Init variables
        L=0

        # Loop over the array
        for R, num in enumerate(nums):
            # Remove previous value if the window is too big
            if (R-L)>k:
                window.remove(nums[L])
                L += 1

            # Check if num is in the window
            if num in window:
                return True

            # Add current value
            window.add(num)

        # Return false if it didnt find it
        return False
            