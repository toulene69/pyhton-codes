
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        if A <= 0:
            return 0
        div = 5
        q = A/div
        i = 1
        while q >=1:
            count += q
            i+=1
            div = 5**i
            q = A/div

        return count


    def fact(self,a):
        f = 1
        for i in range(1,a+1):
            f *= i
        return f
x = 100
obj = Solution()
print obj.trailingZeroes(x)
# print obj.fact(x)