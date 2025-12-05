class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Need all possible combination of k numbers from [1, n]
        res = []

        def dfs(i, path):
            if len(path) == k:
                res.append(path[:])
                return

            if i > n:
                return

            # try every number 
            for j in range(i+1, n+1):
                path.append(j)
                dfs(j, path)
                path.pop()

        dfs(0, [])
        return res