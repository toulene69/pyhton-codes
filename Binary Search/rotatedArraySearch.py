

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)

        s = 0
        e = n-1
        invert = -1
        while s <= e:
            mid = s + ((e-s)>>1)
            if mid < e and A[mid] > A[mid+1]:
                invert = mid+1
                break
            elif mid > s and A[mid] < A[mid-1]:
                invert = mid
                break
            if A[mid] > A[e]:
                s = mid+1
            else:
                e = mid -1
        if invert == -1:
            invert = 0
        i = None
        j = None
        if invert == 0:
            i = 0
            j = n-1
        else:
            if B >= A[invert] and B<=A[n-1]:
                i = invert
                j = n-1
            elif B <= A[invert-1] and B >= A[0]:
                i = 0
                j = invert-1
        while i<=j:
            m = i + (j-i)/2
            if B == A[m]:
                return m
            if B > A[m]:
                i = m+1
            else:
                j = m-1
        return -1




a = [ 4, 5, 6 ,7 ,0 ,1, 2]
b = 2
obj  = Solution()
print obj.search(a,b)