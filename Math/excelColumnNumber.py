"""
Given a column title as appears in an Excel sheet, return its corresponding column number.
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):

        aplpha = {}
        for i in xrange(65,91):
            aplpha[str(unichr(i))] = i - 64
        col = 0
        j = 0
        for i in xrange(len(A)-1,-1,-1):
            val = aplpha[A[i]]
            col += ((26**j)*val)
            j += 1

        return col

    def convertToTitle(self, A):
        """
        26 -> Z
        27 -> AA
        28 -> AB
        :param A: 
        :return: 
        """
        alpha = {}
        for i in xrange(65, 91):
            alpha[i - 64] = str(unichr(i))

        temp = []
        num = A

        while num != 0:
            r = num % 26
            if r == 0:
                temp.append(26)
                num  = num/26 - 1
            else:
               temp.append(r)
               num /= 26
        temp.reverse()
        col = ''
        for item in temp:
            if item in alpha:
                col += alpha[item]
        return col






z = 'ZZ'
obj = Solution()
# x=  obj.titleToNumber(z)
x = 943566
print obj.convertToTitle(x)
