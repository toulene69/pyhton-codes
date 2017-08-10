

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        n = len(A)
        start = None
        end = None
        sumAsOf = -1
        i = 0
        j = 0
        while i<n and j<n:
            if A[j] == 1:
                j+=1
            else:
                B-=1
                j+=1
            while B<0 and i<j:
                if A[i] == 0:
                    B+=1
                i+=1
            if i-j != 0:
                if sumAsOf < (j-i):
                    sumAsOf = j-i
                    start = i
                    end = j-1
        out = []
        if sumAsOf <=0:
            return out
        while start<=end:
            out.append(start)
            start+=1
        return out

a = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
a = [0,1,1,1]
a = [0,0,0,0]
a = [ 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0 ]
b = 4
obj = Solution()
print obj.maxone(a,b)
