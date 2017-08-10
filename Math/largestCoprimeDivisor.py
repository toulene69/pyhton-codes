class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        gcd = self.gcd(A,B)
        if gcd == 1:
            return A
        while gcd != 1:
            A /= gcd
            gcd = self.gcd(A,B)
        return A

    def gcd(self,a,b):
        a , b = max(a,b), min(a,b)
        while b !=0 :
            a = a%b
            a,b = max(a,b), min(a,b)
        return a

a = 30
b = 12
obj = Solution()
print obj.cpFact(a,b)