import sys
class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        temp = A
        multiplier = 1
        num = 0
        while temp != 0:
            num = num * 10 + (temp%10)
            temp /= 10
        if num == A:
            return True
        else:
            return False

    def reverse(self, A):
        """
        # @param A : integer
        # @return an integer
        """
        temp = A

        if A<0:
            negative = True
            temp *= -1
        else:
            negative = False
        multiplier = 1
        num = 0
        while temp != 0:
            num = num * 10 + (temp % 10)
            temp /= 10
        if num > (2**31-1):
            return 0
        if negative:
            num *= -1
        return num


x = 2147447412
obj = Solution()
# print obj.isPalindrome(x)
print obj.reverse(-1146467285)