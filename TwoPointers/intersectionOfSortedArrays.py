
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        m = len(A)
        n = len(B)
        i = j = 0
        out = []
        while i<m and j<n:
            if A[i] == B[j]:
                out.append(A[i])
                i+=1
                j+=1
            elif A[i] < B[j]:
                i+=1
            else:
                j+=1
        return out

a = [1, 2, 3, 3, 4, 5, 6]
b = []
obj = Solution()
print obj.intersect(a,b)