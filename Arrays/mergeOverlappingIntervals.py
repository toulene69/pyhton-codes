class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):

        temp = []
        for item in intervals:
            temp.append([item.start,item.end])
        temp.sort()
        temp_intervals = []
        for item in temp:
            temp_intervals.append(Interval(item[0],item[1]))
        n = len(temp_intervals)
        if n==0 or n== 1:
            return intervals
        first = temp_intervals[0]
        last = temp_intervals[n-1]
        if first.start <= temp_intervals[1].start and first.end >= last.end:
            return [first]
        merged = []
        merged.append(temp_intervals[0])
        i = 0
        for item in temp_intervals[1:]:
            if max(merged[i].start, item.start) > min(merged[i].end,item.end) : # no overlapping interals
                merged.append(item)
                i+=1
            else: #intervals overlap
                curr = merged.pop(i)
                obj = Interval(min(curr.start,item.start), max(curr.end,item.end))
                merged.append(obj)

        for item in merged:
            print [item.start, item.end]

    def merge_temp(self, intervals):

        temp = []
        for item in intervals:
            temp.append([item[0], item[1]])
        temp.sort()
        temp_intervals = []
        for item in temp:
            temp_intervals.append(Interval(item[0], item[1]))
        n = len(temp_intervals)
        if n == 0 or n == 1:
            return intervals
        first = temp_intervals[0]
        last = temp_intervals[n - 1]
        # if first.start <= temp_intervals[1].start and first.end >= last.end:
        #     return [first]
        merged = []
        merged.append(temp_intervals[0])
        i = 0
        for item in temp_intervals[1:]:
            if max(merged[i].start, item.start) > min(merged[i].end, item.end):  # no overlapping interals
                merged.append(item)
                i += 1
            else:  # intervals overlap
                curr = merged.pop(i)
                obj = Interval(min(curr.start, item.start), max(curr.end, item.end))
                merged.append(obj)

        for item in merged:
            print [item.start, item.end]

#[1,3],[2,6],[8,10],[15,18]
i1 = Interval(5,19)
i2 = Interval(2,6)
i3 = Interval(1,10)
i4 = Interval(15,18)
i5 = Interval(17,20)
a = [i2,i1,i3,i4,i5]
b = [ (72, 75), (42, 71), (22, 61), (64, 77), (5, 87), (68, 78), (1, 98), (15, 75), (2, 62), (22, 54), (65, 100), (33, 39), (65, 94), (67, 69), (21, 89), (17, 36), (53, 55), (43, 94), (25, 63), (16, 20), (81, 83), (9, 51), (33, 59), (54, 81), (67, 98), (4, 12), (45, 76), (15, 54), (21, 93), (18, 18), (52, 74), (53, 88), (51, 84), (17, 17), (41, 71), (46, 70), (7, 36), (60, 76), (21, 36), (20, 30), (82, 87), (5, 19), (80, 85), (20, 27), (46, 93), (49, 59), (56, 69), (63, 98), (59, 59) ]
obj = Solution()
obj.merge_temp(b)
