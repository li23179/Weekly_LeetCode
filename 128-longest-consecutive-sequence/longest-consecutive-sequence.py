class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            # check if n-1 on the left of the current number exists
            # if not then current number is the start of the sequence
            if n - 1 not in nums_set:
                length = 1
                # check does it have a successor in the set
                # if yes length++
                while (n + length) in nums_set:
                    length += 1

                longest = max(longest, length)

        return longest