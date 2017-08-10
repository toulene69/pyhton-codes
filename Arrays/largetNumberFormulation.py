class Solution:
    # @param A : tuple of integers
    # @return a strings representing the largest possible number
    def largestNumber(self, A):
        b = sorted(A, cmp=lambda x, y: self.compare(x, y))
        num = ''
        for item in b:
            num += str(item)
        if num[0] == '0':
            return '0'
        return num


    def compare(self,x,y):
        if str(x)+str(y) > str(y)+str(x) :
            return -1
        elif str(x)+str(y) < str(y)+str(x) :
            return 1
        else:
            return 0

a = [3,30,34,5,9]
b = (0,0,0)
#b = sorted(a,cmp= lambda x,y : compare(x,y))
obj = Solution()
print obj.largestNumber(a)


