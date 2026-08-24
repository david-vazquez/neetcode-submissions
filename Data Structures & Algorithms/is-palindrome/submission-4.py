class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Start pointers
        L=0
        R=len(s)-1

        # Check from bought sides
        while L<R:
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue

            if s[L].lower()!=s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        # Return
        return True