class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []

        def dfs(i, cur):
            
            # base case: when cur reaches the target
            if cur == target:
                res.append(sol[:])
                return
            
            # when index out of bound or cur > target
            if i == len(candidates) or cur > target:
                return

            # choose to add the current or not add and skip to the other
            sol.append(candidates[i])
            dfs(i, cur+candidates[i])
            sol.pop()

            dfs(i+1, cur)
        dfs(0, 0)
        return res