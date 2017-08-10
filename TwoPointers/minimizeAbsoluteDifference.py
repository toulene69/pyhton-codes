import sys

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        out = sys.maxint
        i = j = k = 0
        while i< len(A) and j < len(B) and k< len(C):
            mn = min(A[i],B[j],C[k])
            mx = max(A[i],B[j],C[k])
            diff = abs(mx-mn)
            if diff == 0:
                out = 0
                break
            if diff < out:
                out = abs(mx-mn)
            if mn == A[i]:
                i+=1
            elif mn == B[j]:
                j+=1
            else:
                k+=1

        return out


a = [ 1, 4, 5, 8, 10]
b = [ 6, 9, 15 ]
c = [2, 3, 6, 6 ]
obj = Solution()
print obj.solve(a,b,c)