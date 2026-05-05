class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        ZY -> 26*26 + 25 -> 701
        ZZ -> 26*26 + 26 -> 702
        AAA -> 26**2 + 26**1 + 1 -> 703
        """
        res = 0
        
        for i, c in enumerate(reversed(columnTitle)):
            res += 26**i * (ord(c) - ord('A') + 1)

        return res