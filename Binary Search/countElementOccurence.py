class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        n = len(A)
        x = B
        start = 0
        end = n - 1
        flag = False
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == x:
                flag = True
                break
            elif A[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        if flag == False:
            return 0
        i = start
        j = mid - 1
        while i<=j:
            m = (i+j)/2
            if A[m] < x :
                i = m+1
            elif A[m]>x:
                i = m-1
            else:
                j = m-1
        s = max(i,j)
        i = mid+1
        j = end
        while i<=j:
            m = (i+j)/2
            if A[m] < x :
                i = m+1
            elif A[m]>x:
                j = m-1
            else:
                i = m+1
        e = min(i,j)
        return e-s+1

a = [1,1,1,1,1,1,2,2,2,2,2,5,5,5,6,6,6,9]
b = 1
obj = Solution()
print obj.findCount(a,b)