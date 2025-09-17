class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNumeric(c: str) -> bool:
            return ord('A') <= ord(c) <= ord('Z') or \
                   ord('0') <= ord(c) <= ord('9') or \
                   ord('a') <= ord(c) <= ord('z')

        l , r = 0, len(s) - 1
        while l < r:
            
            while not isAlphaNumeric(s[l]) and l < r:
                l += 1
            
            while not isAlphaNumeric(s[r]) and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True