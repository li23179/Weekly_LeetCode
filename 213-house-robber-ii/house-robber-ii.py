class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, nums[0]

        for i in range(1, len(nums)):
            newRob = max(rob1 + nums[i], rob2)
            rob1, rob2 = rob2, newRob

        return rob2