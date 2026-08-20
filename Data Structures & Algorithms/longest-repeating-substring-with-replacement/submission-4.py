class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        L = 0
        maxLength = 0
        maxFreq = 0

        for R in range(len(s)):

            # Add an element to the window
            window[s[R]] = 1 + window.get(s[R], 0)

            # Check if the window is valid
            while (R-L+1)>=max(window.values())+k+1:
                # Remove an element
                window[s[L]] -= 1
                L += 1
            
            # Update the max length
            maxLength = max(maxLength, R-L+1)

        # Return the value
        return maxLength


