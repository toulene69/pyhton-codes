class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        sumHam = 0
        p = 1000000007
        n = len(A)
        mat = {}
        for i in xrange(n):
            for j in xrange(i+1,n):
                if A[i] != A[j]:
                    if (A[i],A[j]) not in mat or (A[j],A[i]) not in mat:
                        temp = 2 *self.findHamming(A[i],A[j])
                        mat[(A[i],A[j])] = temp
                    else:
                        if (A[i],A[j]) in mat:
                            temp = mat[(A[i],A[j])]
                        else:
                            temp = mat[(A[i],A[j])]
                    sumHam += temp
                    sumHam %= p
        return sumHam




    def findHamming(self,a,b):
        x = a^b
        p = 1000000007
        count = 0
        while x != 0:
            if x%2 == 1:
                count += 1
            x /= 2
        return (count % p)


    def sumHammingDistance(self,A):
        bitCount = []
        sumHam = 0
        p = 1000000007
        n = len(A)
        for i in xrange(n):
            num = A[i]
            bi = 0
            while num !=0:
                if num & 1 == 1:
                    if len(bitCount) <= bi:
                        bitCount.append({'x':0,'y':1})
                    else:
                        bitCount[bi]['y'] += 1
                else:
                    if len(bitCount) <= bi:
                        bitCount.append({'x':1,'y':0})
                    else:
                        bitCount[bi]['x'] += 1
                bi+=1
                num = num >>1
        for item in bitCount:
            if item['x'] + item['y'] != n:
                item['x'] = abs(n - item['y'])
        for j in xrange(len(bitCount)):
            sumHam += ( 2 * bitCount[j]['x'] * bitCount[j]['y'] )
            sumHam %= p
        return sumHam
x = [2,4,6]
y = [ 96, 96, 7, 81, 2, 13 ]
z = [ 88, 5, 47, 88, 60, 23 ]
obj = Solution()
print obj.hammingDistance(z)
print obj.sumHammingDistance(z)