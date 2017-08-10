
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        out = ""
        n = len(A)
        m = len(B)
        carry = 0
        i = n- 1
        j = m - 1
        while i >= 0 and j >= 0:
            s = (int(A[i]) + int(B[j]) + carry)
            x = s % 2
            carry = s / 2
            out += str(x)
            i -= 1
            j -= 1
        while i >= 0:
            s = int(A[i]) + carry
            x = s % 2
            carry = s / 2
            out += str(x)
            i -= 1
        while j >= 0:
            s = int(B[j]) + carry
            x = s % 2
            carry = s / 2
            out += str(x)
            j -= 1
        if carry == 1:
            out += '1'
        return out[::-1]


a = "111"
b = "11"
obj = Solution()
print obj.addBinary(a, b)
