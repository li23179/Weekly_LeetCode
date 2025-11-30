class Solution:
    def is_digit(self, c):
        return (ord('0') <= ord(c) and ord(c) <= ord('9'))
    
    def myAtoi(self, s: str) -> int:
        # skip to the all the space char to the first char
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        # check whether i is out of bound
        if i == len(s):
            return 0

        # check is the first char -/+ sign
        negative = False
        if s[i] == '-':
            negative = True
            i += 1
        elif s[i] == "+":
            i += 1

        # check is the current char is invalid
        if i == len(s) or not self.is_digit(s[i]):
            return 0
        
        integer = 0
        # convert the str to integer
        while i < len(s) and self.is_digit(s[i]):
            digit = ord(s[i]) - ord('0')
            integer = integer * 10 + digit
            i += 1

        integer = -integer if negative else integer

        # round it to [-2^31, 2^31-1]
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        
        if integer > INT_MAX:
            integer = INT_MAX
        elif integer < INT_MIN:
            integer = INT_MIN

        return integer