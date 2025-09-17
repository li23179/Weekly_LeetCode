class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            
            while s[r] in s_set and l < r:
                s_set.discard(s[l])
                l += 1
            
            s_set.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest
