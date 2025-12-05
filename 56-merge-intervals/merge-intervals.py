class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            j = i
            # if there is an overlap
            while j + 1 < len(intervals) and end >= intervals[j+1][0]:
                end = max(end, intervals[j+1][1])
                j += 1
            
            res.append([start, end])
            i = j + 1

        return res