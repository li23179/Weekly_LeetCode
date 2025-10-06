class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        [1,2,3,4,5,6,7], k = 3   
                 s
        [7,6,5,4,3,2,1]
            k-1
        [5,6,7,1,2,3,4]
        [5,6,7,1,2,3,4]
        starting position = len(num) - k
        """
        k = k % len(nums)

        self.reverse(0, len(nums)-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums)-1, nums)


    def reverse(self, l, r, nums):
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


        