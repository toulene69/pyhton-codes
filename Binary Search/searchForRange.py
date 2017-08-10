
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

        n = len(A)
        s = 0
        e = n-1
        flag = False
        while s<=e:
            mid = s + (e-s)/2
            if A[mid] == B:
                flag = True
                break
            elif A[mid] < B:
                s = mid+1
            else:
                e = mid-1
        if flag == False:
            return [-1,-1]
        i = 0
        j = mid-1
        while i<=j:
            m = i + (j-i)/2
            if A[m] == B:
                j = m-1
            elif A[m] < B:
                i = m+1
        start = max(i,j)
        i = mid+1
        j = n-1
        while i<=j:
            m = i + (j-i)/2
            if A[m] == B:
                i = m+1
            elif A[m] > B:
                j = m-1
        end = min(i,j)
        return [start,end]


# a = [5, 7, 7, 8, 8, 10]
a = [1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,9,9,9,9,9,9,9]
x = 2
obj = Solution()
print obj.searchRange(a,x)