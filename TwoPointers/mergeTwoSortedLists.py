

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        m = len(A)
        n = len(B)
        i = 0
        j = 0
        out = []
        while i<m and j<n:
            if A[i] <= B[j]:
                out.append(A[i])
                i+=1
            else:
                out.append(B[j])
                j+=1
        if i<m:
            out.extend(A[i:])
        if j<n:
            out.extend(B[j:])
        A=out
        return A


a = [1,4,10]
b = [6,9]
obj = Solution()
print obj.merge(a,b)