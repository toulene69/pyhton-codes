class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        for i in range(n):
            x = A[i]
            k = i
            j = i+1
            while j<n and x == A[j]:
                j += 1
            if (n-j) == x:
                return 1

        return -1


a = [1,1,1,]

obj = Solution()
print obj.solve(a)