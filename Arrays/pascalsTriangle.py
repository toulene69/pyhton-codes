
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A <= 0:
            return  [[]]
        if A == 1:
            return [[1]]
        else:
            pt = [[1]]

            for i in range(1,A):
                temp = []
                for j in range(i+1):
                    preRow = pt[i-1]
                    c = 0
                    cMin1 = 0
                    if j < len(preRow):
                        c = preRow[j]
                    if j-1 >=0:
                        cMin1 = preRow[j-1]
                    temp.append(c+cMin1)
                pt.append(temp)
            return pt
# obj = Solution()
# print obj.generate(3)


class Solution1:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A <= 0:
            return  []
        if A == 1:
            return [1]
        else:
            pt = [[1]]

            for i in range(1,A+1):
                temp = []
                for j in range(i+1):
                    preRow = pt[i-1]
                    c = 0
                    cMin1 = 0
                    if j < len(preRow):
                        c = preRow[j]
                    if j-1 >=0:
                        cMin1 = preRow[j-1]
                    temp.append(c+cMin1)
                pt.append(temp)
            return pt[A]


obj = Solution1()
print obj.getRow(3)