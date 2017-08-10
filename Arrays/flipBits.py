
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        b = []
        try:
            for x in A:
                b.append(int(x))
        except:
            n = len(b)
        sum = 0
        current_max = 0
        start = 0
        end = 0
        l = 0
        for i in range(n):
            item = b[i]
            if item == 1:
                current_max -= 1
            else:
                current_max += 1
            if current_max < 0:
                current_max = 0
                l = 0
            elif sum < current_max:
                sum = current_max
                start = i - l + 1
                end = i + 1
                l += 1
            else:
                l += 1
        if sum > 0:
            print [start, end]
        else:
            print []

a = "1101010001"
b = "1111111"
obj = Solution()
obj.flip(b)
