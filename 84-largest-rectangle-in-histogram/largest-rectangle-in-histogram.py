class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        maxArea = 0
        # pair : (start_position, height)
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stack_i, stack_h = stack.pop()
                maxArea = max(maxArea, (i - stack_i) * stack_h)
                start = stack_i

            stack.append((start, h))
        
        for i, h in stack:
            
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea