class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
                   ki                         j
        if nums[i] > nums[j] => i += 1
        else: 
        nums1 = [2,3,5,6]

        """

        i, j, k = m-1, n-1, m+n-1

        while j >= 0:
            if i < 0 or nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            
            k -= 1