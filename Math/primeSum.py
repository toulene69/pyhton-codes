
'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        sqt = int(A ** 0.5) + 1
        prims = []
        for i in xrange(A + 1):
            prims.append(True)
        prims[0] = False
        prims[1] = False
        for i in xrange(2, sqt):
            j = 2
            if prims[i] == False:
                continue
            while i * j <= A:
                prims[i * j] = False
                j += 1
        for i in xrange(2, A):
            if prims[i] == True and prims[abs(A - i)] == True:
                return [min(i, A - i), max(i, A - i)]
        return []

a = 16777214
obj = Solution()
print obj.primesum(a)
