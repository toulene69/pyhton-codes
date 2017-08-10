class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        maximum = 0
        max_as_of = 0
        max_val = max(A)
        max_array = []
        temp = []
        start_index = 0
        if max_val <=0 :
            max_zeros = 0
            for i in range(n):
                if A[i] == 0:
                    max_as_of += 1
                    temp.append(A[i])
                else:
                    max_as_of = 0
                    temp = []

                if maximum < max_as_of:
                    maximum = max_as_of
                    max_array = temp[:]
            return max_array

        else:
            for i in range(n):
                if A[i] >=0 :
                    max_as_of += A[i]
                    temp.append(A[i])
                else:
                    max_as_of = 0
                    temp = []

                if maximum < max_as_of:
                    maximum = max_as_of
                    max_array = temp[:]
                elif maximum == max_as_of :
                    if len(max_array) < len(temp):
                        max_array = temp[:]


            return max_array


a = [0,0,-1,0,1]
b = [ 336465782, -278722862, -2145174067, 1101513929, 1315634022, -1369133069, 1059961393, 628175011, -1131176229, -859484421 ]

obj = Solution()
print obj.maxset(b)