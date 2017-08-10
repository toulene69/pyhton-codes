
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        temp = [A[x] for x in range(n)]
        dup = -1
        for i in range(n):
            if temp[abs(temp[i])] < 0:
                dup = abs(temp[i])
                break
            else:
                temp[abs(temp[i])] = - temp[abs(temp[i])]
        return dup


a = [1,2,3,4,3]

obj = Solution()
print obj.repeatedNumber(a)