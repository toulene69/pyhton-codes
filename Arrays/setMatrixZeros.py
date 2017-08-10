
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = 0
        if m > 0:
            n = len(A[0])

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    for k in range(n):
                    # mark ith row as -1
                        if A[i][k] != 0:
                            A[i][k] = -1
                    for k in range(m): # mark jth column as -1
                        if A[k][j] != 0:
                            A[k][j] = -1
        # now mark -1 values as 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == -1:
                    A[i][j] = 0
        return A

    def setZero(self,A):
        m = len(A)
        n = len(A[0])

        dict_row = {}
        dict_col = {}

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    dict_row[i] = 1
                    dict_col[j] = 1

        for row in dict_row.keys():
            for j in range(n):
                A[row][j] = 0
        for col in dict_col.keys():
            for i in range(m):
                A[i][col] = 0
        return A


a = [[1, 1, 1,0], [1, 0, 1,1], [0, 1, 1,1]]
b = [[1,0,1],[1,1,1],[1,1,1]]
obj = Solution()
#print obj.setZeroes(a)
print obj.setZero(a)