

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 0
        if n == 0:
            return 1 % d
        a = x % d
        t = 1
        while (n > 0):
            if (n & 1):
                t = (t * a) % d
            n >>= 1
            a = (a * a) % d
        return (t)

    def power(self,x,n):
        if x == 0:
            return 0
        if n == 0:
            return x
        res = 1
        while(n>0):
            if n&1:
                res = (res*x)
            n >>= 1
            x = x*x
        return res

    def power1(self,x,y,d):
        if n==0:
            return 1
        if x ==0:
            return 0
        x = x % d
        res = 1
        while y>0:
            if y&1:
                res = (res * x)%d
                y -= 1
            else:
                x = (x*x)%d
                y /= 2
        return res
x = 71045970
n = 41535484
d = 64735492
obj = Solution()
print obj.pow(x,n,d)
# print obj.power(2,4)