class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        n = len(A)
        if n==0:
            return []
        if n==1:
            return A

        A.sort()
        i = 0
        while i < n:
            if i+1 <n :
                A[i] , A[i+1] = A[i+1], A[i]
                i += 2
            if i == n-1:
                break

        return A



obj = Solution()
a = [-11, 2, 3, 4,5,6]
print obj.wave(a)
