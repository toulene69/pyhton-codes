

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        m = A
        n = B
        dp = [[0]*n for i in xrange(m)]
        for i in xrange(n):
            dp[0][i] = 1
        for i in xrange(m):
            dp[i][0] = 1

        for i in xrange(1,m):
            for j in xrange(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

a = 10
b = 7
obj = Solution()
print obj.uniquePaths(a,b)
