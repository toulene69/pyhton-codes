import sys
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==1:
            return 1
        s = 1
        e = A/2
        diff = sys.maxint
        num = 0
        while s<=e:
            sq = s*s
            if sq == A:
                return s
            elif sq < A:
                num = s
                s *= 2
            else:
                break
        i = num
        j = s
        while i<=j:
            m = (i+j)/2
            diff = (A - (m**2))
            if diff ==0 :
                return m
            elif diff > 0:
                i = m+1
            else:
                j = m-1

        if (A-(m**2))<0:
            return m-1

        return m

x = 17#791503004
obj = Solution()
print obj.sqrt(x)