class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        nums, val
        remove all occurrence of val in nums (in-place)
        return the number of elements in nums not equal to val

        [3,2,2,3] val = 3 k = 2
         k
           i
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
        