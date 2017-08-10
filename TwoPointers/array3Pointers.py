
import sys
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        m, n, o = len(A), len(B), len(C)
        i=j=k=0
        minAsOf = sys.maxint
        while i<m and j<n and k<o:
            mx = max(A[i], B[j], C[k])
            mn = min(A[i], B[j], C[k])
            diff = abs(mx-mn)
            if diff< minAsOf:
                minAsOf = diff
            if mn == A[i]:
                i+=1
            elif mn == B[j]:
                j+=1
            else:
                k+=1
        return minAsOf


a = [1, 4, 10]
b = [2, 15, 20]
c = [10, 12]
obj = Solution()
print obj.minimize(a,b,c)