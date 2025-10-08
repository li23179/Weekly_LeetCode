class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # store the count of each element in a hash map
        nums_dict = defaultdict(int)

        for num in nums:
            nums_dict[num] += 1
        
        res = []
        sol = []

        def dfs(nums_map):

            if all(val == 0 for val in nums_map.values()):
                res.append(sol[:])
                return res

            for num, count in nums_map.items():
                if count > 0:
                    sol.append(num)
                    nums_map[num] -= 1
                    dfs(nums_map)
                    nums_map[num] += 1
                    sol.pop()
        dfs(nums_dict)
        return res
