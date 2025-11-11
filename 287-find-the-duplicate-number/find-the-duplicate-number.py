class Solution:
    """
    Floyd's Tortoise and Hare Algorithm
    Uses fast and slow pointer
    1. detect a cycle
    2. find the start point of the cycle
    There is a prove in the directory, have a look :)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # first pass: to detect the cycle of a linked list
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # second pass: find where is the intersection 
        # (i.e. start point of the cycle)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        return -1