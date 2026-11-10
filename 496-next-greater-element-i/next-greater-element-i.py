class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # use a hash map to store the element corresponds index {nums2[i] : i}
        # nums1 = [4,1,2], nums2 = [1,3,4,2]
        # stack approach = [2, 3] stack[-1] > current, pop the stack, then the remaining is -1
        # nums2 = [2, 3]
        # greater = [-1, -1, -1, -1]
        # then use the hash map to retreive the elements
        stack = []
        mp = {nums2[i] : i for i in range(len(nums2))}

        greater = [-1] * len(nums2)

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                greater[i] = stack[-1]
            stack.append(nums2[i])

        res = []
        for i in range(len(nums1)):
            idx = mp[nums1[i]]
            res.append(greater[idx])

        return res