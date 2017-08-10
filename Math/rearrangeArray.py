class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        for i in xrange(n):
            current_val = A[i]
            new_val = A[A[i]]
            if new_val <0:
                new_val = abs(new_val)/n
            A[i] = (current_val*n + new_val) * -1

        for i in xrange(n):
             A[i] = abs(A[i]) % n

x = [4,1,0,3,2]
y = [1,0]
obj = Solution()
obj.arrange(y)
print y
