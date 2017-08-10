import sys

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):

        n = len(A)
        if B == 0:
            return -1
        if n < B:
            return -1
        if n == B:
            return max(A)

        s = sum(A)
        start = 0
        end = s
        mPages = sys.maxint
        while start<=end:

            mid = start + (end-start)/2
            if self.isPossible(A,B,mid):
                mPages = min(mPages,mid)
                end = mid -1
            else:
                start = mid + 1

        return mPages

    def isPossible(self,a,b,cur_min):

        studRequired = 1
        cur_sum = 0
        for i in xrange(len(a)):
            if a[i] > cur_min:
                return False
            if (cur_sum+a[i]) > cur_min :
                studRequired += 1
                cur_sum = a[i]
                if studRequired > b :
                    return False
            else:
                cur_sum += a[i]
        return True


a = [12, 34, 67, 90]
b = 3
obj = Solution()
print obj.books(a,b)