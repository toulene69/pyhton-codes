class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        m = len(A)
        n = len(A[0])
        t = 0
        b = m - 1
        l = 0
        r = n - 1
        dir = 0  # 0,1,2,3
        while (t <= b and l <= r):
            if (dir == 0):
                x = t
                for y in range(l, r + 1):
                    result.append(A[x][y])
                dir = 1
                t += 1
            elif dir == 1:
                x = t
                y = r
                while x<=b :
                    result.append(A[x][y])
                    x += 1
                dir = 2
                r -= 1
            elif dir == 2:
                x = b
                for y in range(r,l-1,-1):
                    result.append(A[x][y])
                dir = 3
                b -= 1
            elif dir == 3:
                x = b
                y = l
                while x>=t:
                    result.append(A[x][y])
                    x -= 1
                dir = 0
                l += 1

        print result

A = [
  [133, 241, 22, 258, 187, 150, 79, 207, 196, 401, 366, 335, 198],
  [401, 55, 260, 363, 14, 318, 178, 296, 333, 296, 45, 37, 10],
  [112, 374, 79, 12, 97, 39, 310, 223, 139, 91, 171, 95, 126]
]
obj = Solution()
obj.spiralOrder(A)