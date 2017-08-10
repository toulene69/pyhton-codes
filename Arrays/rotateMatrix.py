

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        if n==1:
            return A
        if n==0:
            return []
        end = n-1
        layers = n/2 + 1
        for l in range(layers):
            start = l
            endl = n-l-1
            j = start
            i = l
            while j < endl:
                temp = A[i][j]
                A[i][j] = A[end-j][i]
                A[end-j][i] = A[end-i][end-j]
                A[end-i][end-j] = A[j][end-i]
                A[j][end - i] = temp
                j+=1

        return A

d = []
a = [
    [1, 2,3],
    [ 4,5,6],
    [7,8,9]
]
b = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]
c = [
    [1 ,2 ,3 ,4 ,5],
    [6 ,7 ,8 ,9 ,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
obj = Solution()
print obj.rotate(c)
