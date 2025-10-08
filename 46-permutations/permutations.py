class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
                    [ ]
                   / |  \
                [1] [2] [3]

        """
        res = []
        sol = []

        def dfs(i):
            # base case: when current index out of bound
            if len(sol) == len(nums):
                res.append(sol[:])
                return res
            
            for i in range(len(nums)):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    dfs(i)
                    sol.pop()
        dfs(0)
        return res
            