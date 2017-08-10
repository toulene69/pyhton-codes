
import sys
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        s = 0
        for i in C:
            s+= i

        start = 0
        end = s*B
        time = sys.maxint
        while start <= end:
            mid = start + (end - start) / 2

            if self.isPossible(C,mid,A,B):
                time = min(time,mid)
                end = mid -1
            else:
                start = mid + 1

        return time % 10000003


    def isPossible(self,arr,t,k,timePerBoard):

        numOfPaint = 1
        time = 0
        for i in xrange(len(arr)):
            if (arr[i]*timePerBoard) > t:
                return False
            if (time+(arr[i]*timePerBoard)) > t:
                numOfPaint += 1
                time = (arr[i]*timePerBoard)
                if numOfPaint>k:
                    return False
            else:
                time += (arr[i]*timePerBoard)

        return True


K = 6
T = 10
L = [ 762, 798, 592, 899, 329 ]

obj = Solution()
print obj.paint(K,T,L)