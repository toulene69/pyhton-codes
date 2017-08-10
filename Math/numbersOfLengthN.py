"""
Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if len(A) ==0 and B > 0:
            return 0
        count = 0
        if B == 1:
            for i in xrange(len(A)):
                if A[i] < C:
                    count += 1
                    continue
                else:
                    break
            return count
        n = len(A)
        num = []
        while C != 0:
            num.append(C % 10)
            C = C / 10
        num.reverse()

        if B > len(num):
            return 0

        elif B < len(num):
            if A[0] == 0:
                count = (n -1) * (n ** (B-1))

                return count
            else:
                count = (n ** B)
                return count
        else:
            pos = self.findNum(A,num[0])
            if pos[0] == False:
                if A[0] == 0:
                    count = pos[1] * (n** (B-1))
                    return count
                else:
                    count = (pos[1] + 1) * (n ** (B - 1))
                    return count

            else:
                if A[0] == 0:
                    count = (pos[1] - 1) * (n**(B-1))
                else:
                    count = (pos[1]) * (n**(B-1))
                j = 1
                p = self.findNum(A,num[j])
                while p[0] == True and j<len(num)-2:
                    count += (p[1]+1) * (n**(B-j-1))
                    j += 1
                    p = self.findNum(A,num[j])
                if j == len(num)-2:
                    pl = self.findNum(A,num[j+1])
                    if p[1] >= 0:
                        if p[0] == True:
                            count += (p[1])
                        else:
                            count += p[1]+1
                    else:
                        p1 = self.findNum(A,num[n-2])
                        count /= (p1[1]+1)
                        count *= n
                    return count
                else:
                    count += (p[1]+1) * (n** (B-j-1))
                    return count





    def findNum(self,arr,x):
        for i in xrange(len(arr)):
            if arr[i] < x:
                continue
            elif arr[i] == x:
                return (True,i)
            else:
                return (False,i-1)
        return (False,i)

    def fact(self,n):
        if n ==0:
            return 1
        elif n < 0:
            return 0
        f = 1
        for i in xrange(1,n+1):
            f *= i
        return f


# a = [ 0, 2, 3, 4, 5, 7, 8, 9 ]
b = 5
a = [ 2, 3, 4, 8, 9 ]
c = 23930
obj = Solution()
print obj.solve(a,b,c)