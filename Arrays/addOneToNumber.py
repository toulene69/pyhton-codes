class Solution:
    """
    a number is represented as a list with most significant digit as the head of the list. add 1 to the numeber and return the list
    """
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        x = []
        flag = True
        for i in range(len(A)-1, -1 , -1):
            if (A[i] + 1) / 10 >= 1:
                x.append((A[i] + 1) % 10)
                continue
            else :
                x.append(A[i]+1)
                flag = False
                i-=1
                break
        if len(A) != len(x):
            while i >= 0:
                x.append(A[i])
                i-=1

        if flag:
            x.append(1)
        else:
            while True:
                if x[len(x)-1] ==0:
                    x.pop()
                else:
                    break
        x.reverse()
        print x

a = [ 0, 3, 7, 6, 4, 0, 5, 5, 5 ]
obj = Solution()
obj.plusOne(a)