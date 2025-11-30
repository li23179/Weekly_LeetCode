class Solution:
    def top_down(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i, j):
            # base case: if we used up all the char
            if i == len(s1) and j == len(s2):
                return True

            # if (i, j) already exist then used the cached value
            if (i, j) in dp:
                return dp[(i, j)]

            # recursive case:
            # if s1[i] contribute (i.e. s1[i] == s3[i+j]) then we 
            # search the (i+1, j) path
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True

            # if s2[j] contribute (i.e. s2[j] == s3[i+j]) then we search
            # the (i, j+1) path
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True

            # if both doesn't contribute
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # base case: if the length of s1 + s2 != s3 impossible 
        if len(s1) + len(s2) != len(s3):
            return False
        
        # bottom up:
        # initialise the search grid
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # the last index matches the s3 last char so make sense
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1) , -1, -1):
            for j in range(len(s2), -1, -1):
                
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
                
        return dp[0][0]

            