

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):

        if len(A) == 0:
            return ""
        if len(A) ==1 and len(A[0]) == 0:
            return []
        res = []
        line = []
        wordcount = 0
        for i in xrange(len(A)):
            if (wordcount + len(A[i]) ) <= B:
                wordcount += len(A[i]) + 1
                line.append(A[i])
            else:
                count = 0
                for item in line:
                    count += len(item)
                dif = B-count
                words = len(line)
                j = 0
                if words == 1:
                    while dif > 0:
                        line[j] = line[j] + " "
                        dif -= 1
                else:
                    while dif >0:
                        line[j]  = line[j]+" "
                        j = (j+1)%(words - 1)
                        dif -= 1
                res.append(line)
                line = []
                wordcount = len(A[i]) + 1
                line.append(A[i])
        if len(line) != 0:
            count = 0
            for item in line:
                count += len(item)
            dif = B - count
            words = len(line)
            j = 0
            if words == 1:
                while dif > 0:
                    line[j] = line[j] + " "
                    dif -= 1
            else:
                while dif > 0:
                    line[j] = line[j] + " "
                    j = (j + 1) % (words - 1)
                    dif -= 1
            res.append(line)
        lastLine = res.pop()
        w = 0
        for x in xrange(len(lastLine)):
            lastLine[x] = lastLine[x].strip()
            w += len(lastLine[x])
            if w < B-1:
                lastLine[x] += " "
                w+=1
        d = B-w
        while d>0:
            lastLine[len(lastLine) - 1] += " "
            d-=1
        res.append(lastLine)
        out = []
        for fline in res:
            s = ""
            for words in fline:
                s += words
            out.append(s)
        return out

# w = ["This", "is", "an", "example", "of", "text", "justification."]
w = [ "What", "must", "be", "shall", "be." ]
x = [ "lkgyyrqh", "qrdqusnh", "zyu", "w", "ukzxyykeh", "zmfqafqle", "e", "ajq", "kagjss", "mihiqla", "qekf", "ipxbpz", "opsndtyu", "x", "ec", "cbd", "zz", "yzgx", "qbzaffgf", "i", "atstkrdph", "jgx", "qiy", "jeythmm", "qgqvyz", "dfagnfpwat", "sigxajhjt", "zx", "hwmcgss"]
l = 12
obj = Solution()
print obj.fullJustify(w,l)
