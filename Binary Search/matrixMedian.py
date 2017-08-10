import sys
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):

        mn = sys.maxint
        mx = -sys.maxint - 1
        m = len(A)
        n = len(A[0])
        midElm = 1 + m*n/2
        for i in xrange(m):
            med = A[i][n/2]
            if med < mn:
                mn = med
            if med > mx:
                mx = med

        while mn < mx:
            mid = mn + (mx-mn)/2
            place = 0
            for j in xrange(m):
                s = 0
                e = n-1
                while s<=e:
                    mi = s + (e-s)/2
                    if A[j][mi] == mid :
                        s = mi+1
                    elif A[j][mi] < mid :
                        s = mi+1
                    else:
                        e = mi-1
                place+= s
            if place < midElm:
                mn = mid +1
            else:
                mx = mid

        return mn


a = [[1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]]

b = [[1, 5, 7],
[4, 10, 11],
[8, 11, 12]]

c = [
  [9, 13, 23],
  [9, 12, 15],
  [7, 10, 12]
]

obj = Solution()
print obj.findMedian(c)
