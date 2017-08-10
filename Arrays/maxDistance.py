
class Solution:
    # @param A : tuple of integers
    # @return an integer such that the maximum of j - i subjected to the constraint of A[i] <= A[j].
    # If there is no solution possible, return -1
    def maximumGap(self, A):
        n = len(A)
        if n == 1:
            return 0
        minL = []
        maxR = [0 for x in range(n)]
        minL.append(A[0])
        maxR[n-1] = A[n-1]
        for i in range(1,n):
            minL.append(min(minL[i-1], A[i]) )
        for j in range(n-2,-1,-1):
            maxR[j] = max(maxR[j+1], A[j])

        maximum = -1
        i , j = 0,0
        while j<n and i < n:
            if minL[i] <= maxR[j]:
                maximum = max(maximum, j-i)
                j += 1
            else:
                i += 1

        return maximum


a = (-3, 5, 4, 2,2)
b = (100, 100, 100, 100, 100)
obj = Solution()
print  obj.maximumGap(b)