class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        # XXVIIV
        #     ij
        i = 0
        j = i + 1
        res = 0
        while j < len(s):
            
            if romanMap[s[i]] < romanMap[s[j]]:
                res -= romanMap[s[i]]
            else:
                res += romanMap[s[i]]
            
            i += 1
            j += 1

        return res + romanMap[s[i]]
