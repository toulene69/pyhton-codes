

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):

        s = 0
        e = len(A)-1
        while s<=e:
            m = s + (e-s)/2
            if A[m] == B:
                return m
            elif A[m] > B:
                e = m-1
            else:
                s = m+1
        return max(s,e)


a = [1,2,2,2,3,3,3,5,6]
b = 2
obj = Solution()
print obj.searchInsert(a,b)