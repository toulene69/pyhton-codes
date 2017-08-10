
class Solution:
    # @param A : integer
    # @return a list of list of integers from 1 to n*n in spiral order
    def generateMatrix(self, A):
        n = A
        if n<=0:
            return [[]]
        mat = [[0]*n for i in range(n)]
        l ,r, t, b = 0, n-1, 0, n-1
        val = 1
        dir = 0 # 0,1,2,3
        while l<=r and t<=b:

            if dir == 0:
                i = t
                j = l
                while j<=r :
                    mat[i][j] = val
                    val += 1
                    j+=1
                t += 1
                dir = 1

            elif dir == 1:
                i = t
                j = r
                while i <= b:
                    mat[i][j] = val
                    val += 1
                    i+=1
                r -= 1
                dir = 2

            elif dir == 2:
                i = b
                j = r
                while j>=l :
                    mat[i][j] = val
                    val+=1
                    j -= 1
                b -= 1
                dir = 3
            elif dir == 3:
                i = b
                j = l
                while i>= t:
                    mat[i][j] = val
                    val +=1
                    i -= 1
                l += 1
                dir = 0

        return mat

obj = Solution()
print  obj.generateMatrix(1)
