class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = defaultdict(int)
        n = len(nums)

        for i in range(n):
            diff = target - nums[i] 
            if diff in nums_dict:
                return [i, nums_dict[diff]]
            
            nums_dict[nums[i]] = i

        return []