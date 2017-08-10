

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        # A.sort()
        n = len(A)
        i = 0
        j = 0
        while j<n :
            c = A[j]
            while j<n and A[j] == B:
                j+=1
            if c != B:
                A[i] = c
                i+=1
                j+=1
        return i

a =[4, 1, 1, 2, 1, 3]
b = 1
obj = Solution()
print obj.removeElement(a,b)
