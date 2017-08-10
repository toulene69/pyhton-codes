

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A == 1:
            return "1"
        m = [1]
        for i in xrange(1,A):
            s = len(m)
            j = 0
            temp = []
            while j<s:
                count = 1
                x = m[j]
                while j<s-1 and x == m[j+1]:
                    count+=1
                    j+=1
                temp.append(count)
                temp.append(x)
                j+=1
            m = temp
        s = ""
        for i in xrange(len(m)):
            s += str(m[i])
        return s


obj = Solution()

print obj.countAndSay(6)