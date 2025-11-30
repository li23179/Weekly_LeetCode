class Solution:
    def rob(self, nums: List[int]) -> int:
        # use a dp table store the maximum money that rob
        # up to each house
        dp = [0] * (len(nums) + 1)
        # the maximum of day 0 is we didn't rob
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums)+1):
            # store the maximum of the day ith
            # depend on either not rob or rob
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])

        return dp[-1]
