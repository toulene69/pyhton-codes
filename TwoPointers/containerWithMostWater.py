

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)
        temp = []
        maxAsOf = 0
        i = 0
        while i<n:
            if len(temp)==0 or A[temp[-1]]<=A[i]:
                temp.append(i)
                i+=1
            else:
                tp = temp.pop()
                if len(temp) == 0:
                    area_top =  A[tp] * i
                else:
                    area_top = A[tp] * (i - temp[len(temp)-1] - 2)
                if maxAsOf < area_top:
                    maxAsOf = area_top

        while len(temp)>0:
            tp = temp.pop()
            if len(temp) == 0:
                area_top = A[tp] * i
            else:
                area_top = A[tp] * (i - temp[len(temp)-1] - 2)
            if maxAsOf < area_top:
                maxAsOf = area_top

        return maxAsOf

    def maxArea1(self, A):
        ret = 0
        l = 0
        r = len(A)-1
        while l<r:
            ret = max(ret, (r-l)*min(A[l],A[r]))
            if A[l] <= A[r]:
                l+=1
            else:
                r-=1
        return ret

a = [1]
obj = Solution()
print  obj.maxArea1(a)