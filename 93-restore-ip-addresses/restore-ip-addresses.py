class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # valid IP -> exactly 4 integers separated by dots, 0-255 inclusive, cannot have leading zeros
        res = []

        def is_valid(part):
            if len(part) > 3 or (len(part) > 1 and part[0] == '0'):
                return False
            
            return 0 <= int(part) <= 255
        
        def backtrack(start, parts):
            # if there are 4 segments and all has been used
            if len(parts) == 4 and start == len(s):
                sol = '.'.join(parts)
                res.append(sol)
                return

            # either criteria has been fulfilled but not both
            if len(parts) == 4 or start == len(s):
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start:start+length]

                if is_valid(segment):
                    parts.append(segment)
                    backtrack(start + length, parts)
                    parts.pop()
        
        backtrack(0, [])
        return res
                
