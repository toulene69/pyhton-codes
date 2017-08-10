class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):

        m = len(A)
        n = len(A[0])
        if B < A[0][0]:
            return 0
        if B > A[m-1][n-1]:
            return 0
        sr = 0
        er = m-1
        flag = False
        row = -1
        while sr<=er:
            midr = sr + (er - sr)/2
            if B < A[midr][0]:
                er = midr-1
            elif B > A[midr][n-1]:
                sr = midr+1
            else:
                flag = True
                row = midr
                break
        if flag:
            ret = self.binarySearch(A,row,n,B)
            return ret
        else:
            return 0

    def binarySearch(self,arr,r,c,x):
        s = 0
        e = c-1
        while s<=e:
            m = (s+e)/2
            if arr[r][m] == x:
                return 1
            elif x > arr[r][m]:
                s = m+1
            else:
                e = m-1
        return 0

a = [
  [1,   3,  5,  10],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
x = 50
obj = Solution()
print  obj.searchMatrix(a,x)