

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        x = int(A)
        if x <2:
            return 0
        a = 2
        while x>=2:
            if x & 1:
                return 0
            x = x >> 1
        return 1


x = "3"
obj = Solution()
print obj.power(x)