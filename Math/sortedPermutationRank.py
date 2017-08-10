"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Assume that no characters are repeated.
"""
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n = len(A)
        rank = 1
        for i in xrange(n):
            rank += self.tempRank(A[i:])

        return rank % 1000003


    def tempRank(self,s):
        n = len(s)
        if n == 0:
            return 0
        count = 0
        first = s[0]
        for i in xrange(1,n):
            if s[i] < first:
                count += 1
        return (count * self.fact(n-1))%1000003


    def fact(self,n):
        if n == 0:
            return 1
        f = 1
        for i in range(1,n+1):
            f*= i
        return f % 1000003


s = 'acb'
obj = Solution()
print obj.findRank(s)