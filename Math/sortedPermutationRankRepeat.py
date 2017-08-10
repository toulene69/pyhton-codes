class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n = len(A)
        if n <= 1:
            return 1
        rank = 1
        for i in xrange(n):
            rank = rank + self.subRank(A[i:])

        return rank

    def subRank(self,s):
        n = len(s)
        if n == 0:
            return 0
        d = {}
        small = {}
        count = 0
        sameChar = 1
        for i in xrange(1,n):
            # if s[0] == s[i]:
            #     count += 1
            #     sameChar += 1
            if s[0] > s[i]:
                if s[i] in d:
                    small[s[i]] += 1
                    d[s[i]] += 1
                else:
                    small[s[i]] = 1
                    d[s[i]] = 1
                    count += 1
            else:
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
        repeat = 1
        for k in d:
            repeat *= self.fact(d[k])

        p = (count * self.fact(n-1))/repeat
        # p /= sameChar
        return p % 1000003

    def fact(self,n):
        if n ==0:
            return 1
        f = 1
        for i in range(1,n+1):
            f *= i
        return f % 1000003

x = 'bbaa'
obj = Solution()
print obj.findRank(x)