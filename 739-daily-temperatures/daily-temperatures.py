class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # store [(temp, index)]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex

            stack.append((temp, i))

        while stack:
            stackTemp, stackIndex = stack.pop()
            res[stackIndex] = 0

        return res