class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down dp
        dp = [[0] * n for _ in range(m)]
        
        # initialise the rightmost col
        for i in range(m-1, -1, -1):
            dp[i][-1] = 1

        # initialise the bottommost row
        for j in range(n-1, -1, -1):
            dp[-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
                print(dp[i][j])
        return dp[0][0]