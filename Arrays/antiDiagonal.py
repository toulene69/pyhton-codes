


class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self,a):
        n = len(a)
        if n ==0:
            return []
        if n == 1:
            return a
        dig = [[] for i in range((n-1)*2 + 1)]
        for i in range(n):
            for j in range(n):
                dig[i+j].append(a[i][j])

        return  dig


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3,11], [4, 5, 6,12], [7, 8, 9,13],[21,34,42,44]]
obj = Solution()
print obj.diagonal(b)
