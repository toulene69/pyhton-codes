
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        res = []
        if n == 0:
            return []
        elif n == 1:
            return []
        elif n==2:
            if A[0]>A[1]:
                return [0,1]

        temp = []
        for i in range(n):
            temp.append((A[i],i))
        temp.sort()
        minInd = n
        maxInd = -1
        for i in range(n):
            if temp[i][1] != i:
                minInd = min(minInd, temp[i][1])
                maxInd = max(maxInd, temp[i][1])
        if maxInd != -1 and minInd != n:
            return [minInd,maxInd]
        else:
            return [-1]



a = [1, 2, 3, 4, 5]
obj = Solution()
print obj.subUnsort(a)