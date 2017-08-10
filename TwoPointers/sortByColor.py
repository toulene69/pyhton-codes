
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        i = 0
        j = n-1
        x = i
        while x<n:
            if A[x] == 0:
                A[i], A[x] = A[x], A[i]
                i+=1
            x+=1
        y = j
        while y>=0:
            if A[y] == 2:
                A[j], A[y] = A[y], A[j]
                j-=1
            y-=1


        return A

    def sortColor(self,A):
        n = len(A)
        i=0
        while i<n and A[i] == 0:
            i+=1
        j = i
        k = n-1
        while i<=k:
            if A[i] == 0:
                A[j], A[i] = A[i],A[j]
                j+=1
                i += 1
            elif A[i] == 2:
                A[k], A[i] = A[i], A[k]
                k-=1
            else:
                i += 1

        return A



# a = [0,1,0,2,2,1,1,0,0,1,2]
# a = [0, 1, 2, 0, 1, 2]
a = [ 2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 1]
# a = [2,2,2,1,1,1]
obj = Solution()
print obj.sortColor(a)