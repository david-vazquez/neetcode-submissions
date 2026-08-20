class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        L = 0
        maxLength = 0

        for R in range(len(s)):

            # Add an element to the window
            if s[R] in window:
                window[s[R]] += 1
            else:
                window[s[R]] = 1

            # Check if the window is valid
            while (R-L+1)>=max(window.values())+k+1:
                # Remove an element
                if window[s[L]]>0:
                    window[s[L]] -= 1
                else:
                    del window[s[L]]
                L += 1
            
            # Update the max length
            maxLength = max(maxLength, R-L+1)

        # Return the value
        return maxLength


