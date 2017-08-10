'''
remove the duplicates in place such that each element can appear atmost twice and return the new length
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        i = 0
        j = 0
        while j<n:
            c = A[j]
            temp = j
            while j<n and c == A[j]:
                j+=1
            if j-temp >= 2:
                A[i] = A[i+1] = c
                i+=2
            else:
                A[i] = c
                i+=1
        return i

a = [1,2,3,3,3,3,4,4,5,5]
obj = Solution()
print obj.removeDuplicates(a)

