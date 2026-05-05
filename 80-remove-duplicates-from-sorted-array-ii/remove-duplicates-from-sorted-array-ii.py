class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i, l, r = 0, 0, 0
        while r < len(nums):
            r = l + 1

            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            
            if r - l > 1:
                nums[i], nums[i+1] = nums[l], nums[l]
                i += 2
            else:
                nums[i] = nums[l]
                i += 1
            
            l = r
        
        return i

            

            
                

