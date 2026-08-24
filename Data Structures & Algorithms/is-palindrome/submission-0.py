class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Clean array
        word = ''
        for c in s:
            if c.isalnum():
                word += c.lower()

        # Start pointers
        L=0
        R=len(word)-1

        # Check from bought sides
        while L<R:
            if word[L]!=word[R]:
                return False
            L += 1
            R -= 1
        
        # Return
        return True