class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Start variables
        window = set()
        L = 0
        maxLength = 0

        # Move the window
        for R in range(len(s)):

            # Check if the new value is already in the window
            while s[R] in window:
                window.remove(s[L])
                L += 1
            
            # Add the value
            window.add(s[R])
            maxLength = max(maxLength, R-L+1)
        
        return maxLength



