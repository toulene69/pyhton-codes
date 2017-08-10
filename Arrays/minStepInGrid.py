class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        n = len(X)
        distance = 0
        for i in range(n-1):
            distance += max(abs(X[i] - X[i+1]), abs(Y[i] - Y[i+1]))
        print distance

x = [0,1,1]
y = [0,1,2]
obj = Solution()
obj.coverPoints(x,y)