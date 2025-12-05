class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        i = 0
        new_start, new_end = newInterval
        
        # add all interval that end < new_start
        while i < len(intervals) and intervals[i][1] < new_start:
            res.append([intervals[i][0], intervals[i][1]])
            i += 1

        # right now we encounter the end > new_start
        # so we find the merged end time for the interval

        # if the new_end > current end_time then merge it
        while i < len(intervals) and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        
        res.append([new_start, new_end])

        # add all the interval that new_end < interval[0]
        while i < len(intervals) and new_end < intervals[i][0]:
            res.append([intervals[i][0], intervals[i][1]])
            i += 1

        return res