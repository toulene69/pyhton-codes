"""
Given a positive integer which fits in a 32 bit signed integer, 
find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
"""
import sys
class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 1:
            return True
        allPrimes = self.pimes(int(A**0.5))
        n = A
        factors = []
        while n != 1:
            found = False
            for j in xrange(len(allPrimes)-1,-1,-1):
                if n%allPrimes[j] == 0:
                    factors.append(allPrimes[j])
                    n = n/allPrimes[j]
                    found = True
                    break
            if found == False:
                factors.append(n)
                break
        if len(factors) == 0:
            return False

        i = 0
        fre = []
        while i <len(factors):
            j = i+1
            temp = 1
            while j < len(factors) and factors[i] == factors[j]:
                temp +=1
                j+=1
            i = j
            fre.append(temp)
        # factors.sort()
        gc = fre[0]
        i = 0
        while i < len(fre)-1:
            gc = self.gcd(gc,fre[i+1])
            if gc == 1:
                break
            i+=1
        if gc >1:
            return True
        else:
            return False

    def pimes(self,a):
        p = []
        for i in xrange(a+1):
            p.append(True)
        p[0] = False
        p[1] = False
        sqt = int(a**0.5)+1
        for i in xrange(2,sqt):
            if p[i] != False:
                j = 2
                while i*j < len(p):
                    p[i*j] = False
                    j+=1
        res = [x for x in xrange(len(p)) if p[x] == True]
        return res

    def gcd(self,a,b):
        a , b = max(a,b), min(a,b)
        while b!= 0:
            temp = a-b
            a, b = max(temp,b), min(temp,b)
        return a

    def isPower2(self,A):
        if A == 1:
            return True
        base = 2
        while base< A and base < sys.maxint/base :
            temp = base
            while temp <= A and temp < sys.maxint/base :
                temp *= base
                if temp == A:
                    return True
            base += 1
        return False

obj = Solution()
# print obj.isPower(7988)
# print obj.isPower2(216000)
print obj.gcd(1,0)