class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        sqt = int(A**0.5)+1
        temp1 = []
        temp2 = []
        for i in range(1,sqt):
            if A%i == 0:
                temp1.append(i)
                if i != A/i:
                    temp2.append(A/i)
        temp2.reverse()
        temp1.extend(temp2)
        return temp1

    def isPrime(self, A):
        if A==1:
            return 0
        sqt = int(A ** 0.5) + 1
        for i in range(2, sqt):
            if A % i == 0:
                return 0
        return 1

    def sieve(self, A):
        if A == 1:
            return []
        nums = {}
        for i in range(2,A+1):
            nums[i] = 1
        sqt = int(A** 0.5) + 1
        for i in range(2,sqt):
            j = 2
            while i*j <= A :
                if i*j in nums:
                    del nums[i*j]
                j+=1
        prims = nums.keys()
        prims.sort()
        return prims

    def findDigitsInBinary(self, A):
        '''
        # @param A : integer
        # @return a strings
        '''
        if A == 0:
            return '0'
        elif A == 1:
            return '1'
        else:
            binary = ''
            while A != 0:
                binary += str(A%2)
                A /= 2
            x =  binary[::-1]
            return x

    def squareSum(self, A):
        ans = []
        mat = {}
        a = 0
        while a * a < A:
            b = 0
            while b * b < A:
                if a * a + b * b == A:
                    if (a, b) not in mat and (b, a) not in mat:
                        newEntry = [a, b]
                        mat[(a, b)] = 1
                        ans.append(newEntry)
                b += 1
            a += 1
        return ans

a = 1
obj = Solution()
#print  obj.allFactors(a)
#print  obj.isPrime(a)
#print obj.sieve(a)
#print obj.findDigitsInBinary(5)
print obj.squareSum(5)