

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        out = []
        i = 0
        while i<len(A):
            j = i+1
            k = len(A)-1
            while j<k:
                s = A[i]+A[j]+A[k]
                if s == 0:
                    if [A[i],A[j],A[k]] not in out:
                        out.append([A[i],A[j],A[k]])
                    j+=1
                if s< 0:
                    j+=1
                else:
                    k-=1
            i+=1
        return out


a = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print obj.threeSum(a)