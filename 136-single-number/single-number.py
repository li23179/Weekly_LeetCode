class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # we can actually find the unique numbers
        res = 0
        for num in nums:
            res = res ^ num
        
        return res