
class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        count = 0
        i = 0
        while i<len(A):
            j = i + 1
            k = i + 2
            while j<len(A):
                if k<=j:
                    k = j+1
                if k<len(A):
                    start = k
                    end = len(A)-1
                    while start <= end:
                        mid = start + (end-start)/2
                        if A[i]+A[j] > A[mid]:
                            start = mid+1
                        else:
                            end = mid-1
                    k = min(start,end)
                    count = count+(k-j)% 1000000007
                j += 1
            i+=1
        return count

    def nTriang1(self, A):
        A.sort()
        count = 0
        i = 0
        while i<len(A):
            j = i + 1
            k = i + 2
            while j<len(A):
                while k<len(A) and A[i]+A[j]>A[k]:
                    k+=1
                count = count+(k-j-1)% 1000000007
                j += 1
            i+=1
        return count


a = [ 4, 6, 13, 16, 20, 3, 1, 12 ]
obj = Solution()
print obj.nTriang1(a)