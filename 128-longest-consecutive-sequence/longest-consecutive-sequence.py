class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # {100, 4, 200, 1, 3, 2}
        #       3

        s = set(nums)
        longest = 0

        for num in s:
            if not num - 1 in s:
                length = 1

                while num + length in s:
                    length += 1

                longest = max(longest, length)

        return longest
                

