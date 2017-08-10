
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        n = len(intervals)
        set = []
        if n ==0:
            return [new_interval]
        if new_interval.end < intervals[0].start:
            set.append(new_interval)
            set.extend(intervals)
            return set
        if new_interval.start > intervals[n-1].end:
            intervals.append(new_interval)
            return intervals
        if new_interval.start <= intervals[0].start and new_interval.end >= intervals[n-1].end:
            return [new_interval]

        s = self.searchInterval(intervals, new_interval,n)
        l, r = s[1], s[2]
        ret = s[0]
        set = []
        if l and r:
            for i in range(ret[0]):
                set.append(intervals[i])
            if intervals[ret[0]].start <= new_interval.start :
                start =  intervals[ret[0]].start
            else:
                start = new_interval.start
            if intervals[ret[1]].end > new_interval.end :
                end =  intervals[ret[1]].end
            else:
                end = new_interval.end
            set.append(Interval(start, end))
            for i in range(ret[1]+1,n):
                set.append(intervals[i])
            return set
        elif l == False and r == True:
            for i in range(ret[0]):
                set.append(intervals[i])
            obj = Interval(new_interval.start, intervals[ret[1]].end)
            set.append(obj)
            for i in range(ret[1]+1,n):
                set.append(intervals[i])
            return set
        elif r == False and l == True:
            for i in range(ret[0]):
                set.append(intervals[i])
            obj = Interval(intervals[ret[0]].start, new_interval.end)
            set.append(obj)
            for i in range(ret[1],n):
                set.append(intervals[i])
            return set
        else:
            for i in range(ret[0] ):
                set.append(intervals[i])

            set.append(Interval(new_interval.start, new_interval.end))
            for i in range(ret[1],n):
                set.append(intervals[i])
            return set


    def merge(self,intervals,new_interval):
        x = []
        flag = False
        for i  in range(len(intervals)):
            if max(new_interval.start,intervals[i].start) > min(new_interval.end,intervals[i].end) :
                x.append(intervals[i])
            else:
                flag = True
                temp = []
                while i<len(intervals) and ( max(new_interval.start,intervals[i].start) < min(new_interval.end,intervals[i].end)):
                    temp.append(intervals[i])
                    i+=1
                if len(temp) != 0:
                    start = temp[0]
                    end = temp.pop()
                    obj = Interval( min(start.start,new_interval.start) , max(end.end, new_interval.end) )
                    x.append(obj)
        if flag == False:
            if new_interval.start > x[len(x)-1].end:
                x.append(new_interval)
            elif new_interval.end < x[0].start:
                x.insert(0,new_interval)
        for item in x:
            print [item.start,item.end]

    def searchInterval(self,intervals,item,n):
        i = 0
        j = n-1
        ret = []
        l = False
        r = False
        while i<=j:
            mid = (i + j)/2
            if item.start < intervals[mid].start :
                j = mid - 1
            elif item.start > intervals[mid].end:
                i = mid + 1
            else:
                ret.append(mid)
                l = True
                break
        if l == False:
            ret.append(i)
        i,j, mid = 0, n-1, 0
        while i<=j:
            mid = (i+j)/2
            if item.end < intervals[mid].start :
                j = mid - 1
            elif item.end > intervals[mid].end:
                i = mid + 1
            else:
                ret.append(mid)
                r = True
                break
        if r == False:
            ret.append(i)
        return (ret,l,r)



# [1,2],[3,5],[6,7],[8,10],[12,16]
i1 = Interval(31935139,38366404)
i2 = Interval(54099301,76986474)
i3 = Interval(87248431,94675146)
i4 = Interval(8,10)
i5 = Interval(12,16)
n = Interval(38366401,54000001)
a = [i1,i2,i3]
obj = Solution()
set= obj.insert(a,n)
for item in set:
    print [item.start, item.end]

#(6037774, 6198243) (6726550, 7004541) (8842554, 10866536) (11027721, 11341296) (11972532, 14746848) (16374805, 16706396) (17557262, 20518214) (22139780, 22379559) (27212352, 28404611) (28921768, 29621583) (29823256, 32060921) (33950165, 64859907) (36210193, 64859907) (36210193, 64859907) (36210193, 64859907) (36210193, 64859907) (36210193, 64859907) (36210193, 64859907) (36210193, 64859907) (36210193, 64859907) (36210193, 64859907) (65277782, 65296274) (67497842, 68386607) (70414085, 73339545) (73896106, 75605861) (79672668, 84539434) (84821550, 86558001) (91116470, 92198054) (96147808, 98979097)
#(6037774, 6198243) (6726550, 7004541) (8842554, 10866536) (11027721, 11341296) (11972532, 14746848) (16374805, 16706396) (17557262, 20518214) (22139780, 22379559) (27212352, 28404611) (28921768, 29621583) (29823256, 32060921) (33950165, 64859907) (65277782, 65296274) (67497842, 68386607) (70414085, 73339545) (73896106, 75605861) (79672668, 84539434) (84821550, 86558001) (91116470, 92198054) (96147808, 98979097)