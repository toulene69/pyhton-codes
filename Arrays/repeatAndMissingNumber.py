
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        b = list(A)
        b.sort()
        expectedSum, actualSum = 0, 0
        last = 0
        duplicate = 0
        if n%2 ==0:
            expectedSum = (n/2) * (n+1)
        else:
            expectedSum = ((n+1) / 2) * (n)
        for item in b:
            actualSum += item
            if last == item:
                duplicate = item
            else:
                last = item
        print [duplicate, duplicate + (expectedSum-actualSum)]

    def repeatedNumber1(self, A):
        n = len(A)
        #b = A[:]
        #b.sort()
        expectedSum, actualSum = 0, 0
        expectedMul, actualMul = 1,1
        last = 0
        duplicate = 0
        if n%2 ==0:
            expectedSum = (n/2) * (n+1)
        else:
            expectedSum = ((n+1) / 2) * (n)
        i =1
        for item in A:
            actualSum += item
            actualMul *= item
            expectedMul *= i
            i+=1
            # if last == item:
            #     duplicate = item
            # else:
            #     last = item
        y = expectedMul/actualMul
        x = (expectedSum - actualSum) / (1- y)
        print x,y
        # print [duplicate, duplicate + (expectedSum-actualSum)]

a = (1,2,3,3,5)
obj = Solution()
obj.repeatedNumber(a)