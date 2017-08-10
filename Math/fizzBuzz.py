
class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):

        out = []
        for i in xrange(1,A+1):
            if i % 15 == 0:
                out.append("FizzBuzz")
            elif i% 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out



obj = Solution()
print obj.fizzBuzz(4)