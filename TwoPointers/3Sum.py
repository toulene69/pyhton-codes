import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        if len(A)<3:
            return 0
        A.sort()
        i = 0
        j = len(A)-1
        out = sys.maxint
        diff = sys.maxint
        temp = []
        for i in xrange(len(A)):
            for j in xrange(i+1,len(A)):
                temp.append(A[i]+A[j])
        temp.sort()
        while i<len(A):
            ind = self.search(temp,B-A[i])
            if temp[ind] == (B-A[i]):
                out = B
                break
            else:
                if abs(B - (temp[ind]+A[i])) < diff:
                    diff = abs(B - (temp[ind]+A[i]))
                    out = temp[ind]+A[i]
            i+=1
        return out

    def search(self,arr,x):
        i = 0
        j = len(arr)-1
        while i<j:
            mid = i + (j-i)/2
            if x==arr[mid]:
                return mid
            elif x< arr[mid]:
                j = mid-1
            else:
                i = mid+1
        return i

    def threeSumClosestA(self, A, B):
        if len(A)<3:
            return -1
        A.sort()
        i = 0
        out = sys.maxint
        diff = sys.maxint
        while i<len(A)-2:
            j = i+1
            k = len(A)-1
            while j<k:
                currentSum = A[i]+A[j]+A[k]
                targetDiff = abs(B-currentSum)
                if targetDiff == 0:
                    return currentSum
                if targetDiff < diff:
                    diff = targetDiff
                    out = currentSum
                if currentSum < B:
                    j+=1
                else:
                    k-=1
            i+=1
        return out
a = [5, -2, -1, -10, 10]
z = [ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ]
b = -1
obj = Solution()
print obj.threeSumClosestA(z,b)
