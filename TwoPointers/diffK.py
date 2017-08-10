

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i = 0
        j = i+1
        n = len(A)
        while i < n and j<n:
            if i >= j:
                j = i+1
            if j<n and abs(A[i] - A[j]) == B:
                return 1
            elif j<n and abs(A[i] - A[j]) > B:
                i+=1
            else:
                j+=1

        return 0


a = [1, 2, 2, 3, 4]
b = 3
obj = Solution()
print obj.diffPossible(a,b)