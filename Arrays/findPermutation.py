'''
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.

Notes
- Length of given string s will always equal to n - 1

Input 1:

n = 3

s = ID

Return: [2, 3, 1]

'''


class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        n = B
        if n == 1:
            return [1]
        if n==0:
            return []

        d = 0
        i = 0
        for char in A:
            if char == 'D':
                d += 1
            else:
                i += 1
        numD = []
        numI = []
        for j in range(i):
            numI.append(n-j)
        for j in range(1,d+1):
            numD.append(j)
        if i == 0:
            numD.append(n)
            numD.reverse()
            return numD
        if d == 0:
            numI.append(1)
            numI.reverse()
            return numI
        res = []
        leftout = numI[i-1] -1
        res.append(leftout)
        for char in A:
            if char == 'D':
                res.append(numD.pop())
            else:
                res.append(numI.pop())
        return res


a = 'DDDI'
b = 5
obj = Solution()
print  obj.findPerm(a,b)